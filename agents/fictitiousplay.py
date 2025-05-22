from itertools import product
import numpy as np
from functools import reduce
from numpy import ndarray
from base.agent import Agent
from base.game import SimultaneousGame, AgentID

class FictitiousPlay(Agent):
    

    def __init__(self, game: SimultaneousGame, agent: AgentID, initial=None, seed=None) -> None:
        super().__init__(game=game, agent=agent)
        np.random.seed(seed=seed)
        
        self.count: dict[AgentID, ndarray] = initial if initial is not None else {
                agent : np.random.randint(low=1, high=3, size=self.game.num_actions(agent)) 
                    for agent in game.agents
            }

        self.learned_policy: dict[AgentID, ndarray] = {
            agent : self.count.get(agent) / np.sum(self.count.get(agent))
                for agent in game.agents
        }
        self.agent = agent


    def get_rewards(self) -> dict:
        g = self.game.clone()
        agents_actions = list(map(lambda agent: list(g.action_iter(agent)), g.agents))
        rewards: dict[tuple, float] = {}
        for actions in product(*agents_actions):
            g.reset()
            g.step(dict(zip(g.agents, actions)))
            rewards[actions] = g.reward(self.agent)
        return rewards
    

    def get_utility(self):
        rewards = self.get_rewards()
        utility = np.zeros(self.game.num_actions(self.agent))
        for action in range(self.game.num_actions(self.agent)):
            for actions in rewards.keys():
                agent_action_mapping = dict(zip(self.game.agents, actions))
                if actions[self.game.agent_name_mapping[self.agent]] == action:
                    reward = rewards[actions]
                    prob = reduce(lambda x, y: x * y, [self.learned_policy[agent][agent_action_mapping[agent]] for agent in self.game.agents if agent != self.agent])
                    utility[action] += reward * prob
        return utility
    

    def bestresponse(self):
        return np.argmax(self.get_utility())
     

    def update(self) -> None:
        try:
            actions = self.game.observe(self.agent)
        except:
            return
        if actions is None:
            return
        for agent in self.game.agents:
            self.count[agent][actions[agent]] += 1
            self.learned_policy[agent] = self.count[agent] / np.sum(self.count[agent])


    def action(self):
        self.update()
        return self.bestresponse()
    

    def policy(self):
       return self.learned_policy[self.agent]
    