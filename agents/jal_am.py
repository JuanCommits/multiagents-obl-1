from base.agent import Agent
from base.game import SimultaneousGame, AgentID

import random
import numpy as np
from itertools import product


class JointActionLearningActionModelling(Agent):

    def __init__(
        self,
        game:SimultaneousGame,
        agent: AgentID,
        learning_rate: float = 0.1,
        discount_factor: float = 0.9,
        exploration_prob: float =1.0, 
        exploration_decay: float=0.9999,
        min_epsilon: float = 0.1,
        seed: int = 42
    ) -> None:
        np.random.seed(seed)
        random.seed(seed)
        self.game = game
        self.agent = agent
        self.q_table = dict()
        self.oponent_count = {
            agent: {} for agent in game.agents if agent != self.agent
        }
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_prob
        self.exploration_decay = exploration_decay
        self.min_epsilon = min_epsilon
        

    def action(self) -> int:
        """
        Select an action using the epsilon-greedy strategy based on the Q-table.
        If the Q-table does not contain the current state, initialize it with zeros for each joint-action.
        """
        current_state = self._get_current_hashable_state()

        if self.q_table.get(current_state) is None:
            self._initialize_q_for_state(current_state)

        # Select epsilon-greedy action based on the Q-table
        action = np.argmax(self.policy())
        if random.random() < self.epsilon:
            action = random.choice(range(self.game.num_actions(self.agent)))

        self.last_state = current_state

        return action
    

    def _initialize_q_for_state(self, state: str) -> None:
        all_actions = [list(self.game.action_iter(agent)) for agent in self.game.agents]
        self.q_table[state] = {
            joint_action:0 
                for joint_action in product(*all_actions)
        }


    def policy(self):
        policy = np.zeros(self.game.num_actions(self.agent))
        state = self._get_current_hashable_state()

        if self.q_table.get(state) is None:
            self._initialize_q_for_state(state)

        
        # Set the action with the highest AV to 1
        action_values = [self._action_value(state, action) for action in range(self.game.num_actions(self.agent))]
        selected_action = np.argmax(action_values) if np.max(action_values) > 0 else random.choice(range(self.game.num_actions(self.agent)))
        policy[selected_action] = 1
        return policy


    def update(self) -> None:
        last_joint_action = self.game.observe_action(self.agent)

        if self.last_state is None or last_joint_action is None:
            return

        self._update_oponent_count()

        # get the current state, last action and last reward
        current_state = self._get_current_hashable_state()
        last_reward = self.game.reward(self.agent)

        if self.q_table.get(current_state) is None:
            self._initialize_q_for_state(current_state)

        # calculate the action value for each action in the current state and get the max action value
        action_values = [self._action_value(current_state, action) for action in range(self.game.num_actions(self.agent))]
        max_action_value = np.max(action_values)

        # update the Q-table
        td_target = last_reward + self.gamma * max_action_value
        td_error = td_target - self.q_table[self.last_state][last_joint_action]
        self.q_table[self.last_state][last_joint_action] += self.alpha * td_error

        self._update_epsilon()


    def _action_value(self, state: str, action: int) -> float:
        """
        Get the action value for a given state and action.
        """
        action_value = 0
        
        agents_actions = list(map(lambda agent: list(self.game.action_iter(agent)), self.game.agents))
        for joint_action in product(*agents_actions):
            joint_action_map = dict(zip(self.game.agents, joint_action))
            if joint_action[self.game.agent_name_mapping[self.agent]] != action:
                continue
            
            q_value = self.q_table[state][joint_action]
            action_value += q_value * self._pi_oponents(joint_action_map, state)

        return action_value
        

    def _pi_oponents(self, joint_action: dict, state: str) -> float:
        p = 1
        for oponent, oponent_action in joint_action.items():
            if oponent != self.agent:
                p *= self._get_oponent_policy(oponent, state)[oponent_action]
        return p


    def reset(self) -> None:
        """Reset the agent's state."""
        self.q_table = dict()
        self.oponent_count = {
            agent: {}
                for agent in self.game.agents if agent != self.agent
        }
        self.last_state = None
        self.epsilon = 1.0
        self._update_epsilon()


    def _update_oponent_count(self) -> None:
        """Update the count of actions taken by the oponent."""
        joint_action = self.game.observe_action(self.agent)
        state = self._get_current_hashable_state()
        if joint_action is None or state is None:
            return
        for oponent in self.game.agents:
            if oponent == self.agent:
                continue
            oponent_action = joint_action[self.game.agent_name_mapping[oponent]]

            if self.oponent_count[oponent].get(state) is None:
                self.oponent_count[oponent][state] = {}
            if self.oponent_count[oponent][state].get(oponent_action) is None:
                self.oponent_count[oponent][state][oponent_action] = 0
            self.oponent_count[oponent][state][oponent_action] += 1
    

    def _get_current_hashable_state(self) -> str:
        """Get the current state of the agent in a hashable format."""
        return self._make_obs_hashable(self.game.observe(self.agent))


    def _make_obs_hashable(self, obs: dict) -> str:
        """Convert the observation to a hashable string."""
        return str(obs)
    

    def _update_epsilon(self) -> None:
        """Decay the exploration probability."""
        self.epsilon *= self.exploration_decay
        self.epsilon = max(self.epsilon, self.min_epsilon)


    def _get_oponent_policy(self, oponent: AgentID, state: str) -> str:
        """Get the policy of an oponent."""
        if self.oponent_count.get(state) is None or \
                sum(self.oponent_count[state][oponent]) == 0:
            return np.ones(self.game.num_actions(oponent)) / self.game.num_actions(oponent)
        
        return self.oponent_count[state][oponent] / sum(self.oponent_count[state][oponent])
