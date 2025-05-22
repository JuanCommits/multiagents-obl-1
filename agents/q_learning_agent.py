import random
import numpy as np
from base.game import SimultaneousGame, AgentID

from base.agent import Agent

class QLearningAgent(Agent):
    def __init__(
        self,
        game:SimultaneousGame,
        agent: AgentID,
        learning_rate: float = 0.3,
        discount_factor: float = 0.9,
        exploration_prob: float = 1.0,
        exploration_decay: float = 0.995,
        min_epsilon: float = 0.1,
        seed: int = 42
    ) -> None:
        np.random.seed(seed)
        random.seed(seed)
        self.game = game
        self.alpha = learning_rate
        self.gamma = discount_factor
        self.epsilon = exploration_prob
        self.agent = agent
        self.q_table = dict()
        self.prev_state = None
        self.last_action = None
        self.exploration_decay = exploration_decay
        self.min_epsilon = min_epsilon



    def policy(self) -> np.ndarray:
        state = self._get_current_hashable_state()

        # Initialize the policy with zeros
        policy = np.zeros(self.game.num_actions(self.agent))

        # Set the action with the highest Q-value to 1
        if state in self.q_table:
            selected_action = np.argmax(self.q_table[state])
        else:
            selected_action = random.choice(range(self.game.num_actions(self.agent)))
        policy[selected_action] = 1

        return policy
    

    def action(self) -> int:
        """
        Select an action using the epsilon-greedy strategy based on the Q-table.
        If the Q-table does not contain the current state, initialize it with zeros.
        """
        current_state = self._get_current_hashable_state()

        # Initialize the Q-value for the current state if it doesn't exist
        if current_state not in self.q_table:
            self.q_table[current_state] = np.zeros(self.game.num_actions(self.agent))

        # Select epsilon-greedy action based on the Q-table
        if random.random() < self.epsilon:
            action = random.choice(range(self.game.num_actions(self.agent)))
        else:
            action = np.argmax(self.q_table[current_state])

        self.last_action = action
        self.prev_state = current_state

        return action
    
    
    def _update_epsilon(self) -> None:
        """Decay the exploration probability."""
        self.epsilon = max(self.epsilon * self.exploration_decay, self.min_epsilon)


    def update(self) -> None:
        """Update the Q-table using the Bellman equation."""
        # Ignore learning if the previous state is None
        if self.prev_state is None or self.last_action is None:
            return
        
        # Get the current state and reward
        current_state = self._get_current_hashable_state()
        reward = self.game.reward(self.agent)

        # Initialize the Q-value for the current state if it doesn't exist
        if current_state not in self.q_table:
            self.q_table[current_state] = np.zeros(self.game.num_actions(self.agent))

        # Get the maximum Q-value for the current state (for TD target)
        max_next_q = np.max(self.q_table[current_state])

        # Calculate the TD target and TD error
        td_target = reward + self.gamma * max_next_q
        td_error = td_target - self.q_table[self.prev_state][self.last_action]

        # Update the Q-value for the previous state-action pair
        self.q_table[self.prev_state][self.last_action] += self.alpha * td_error

        self._update_epsilon()


    def reset(self) -> None:
        """Reset the agent's state."""
        self.prev_state = None
        self.last_action = None
        self.epsilon = 1.0
        self.q_table = dict()
        self.game.reset()


    def _get_current_hashable_state(self) -> str:
        """Get the current state of the agent in a hashable format."""
        return str(self.game.observe(self.agent))


    def _make_obs_hashable(self, obs: dict) -> str:
        """Convert the observation to a hashable string."""
        return str(obs)
