import numpy as np

from base.game import SimultaneousGame, AgentID
from base.agent import Agent


class RegretMatching(Agent):

    def __init__(self, game:SimultaneousGame, agent: AgentID, seed: int) -> None:
        np.random.seed(seed=seed)
        self.game = game
        self.agent = agent

        self.acum = np.ones(self.game.num_actions(agent))


    def update(self) -> None:
        try:
            actions = self.game.observe(self.agent)
        except:
            return

        if actions is None:
            return

        regrets = self.calculate_regrets(actions)
        self.acum += regrets
                

    def calculate_regrets(self, actions: dict) -> np.ndarray:
        game_clone = self.game.clone()
        regrets = np.zeros(self.game.num_actions(self.agent))

        for action in range(self.game.num_actions(self.agent)):
            game_clone.reset()
            action_copy = actions.copy()
            action_copy[self.agent] = action
            game_clone.step(action_copy)
            regrets[action] =  game_clone.reward(self.agent) - self.game.reward(self.agent)

        return regrets


    def action(self):
        probs = self.policy()
        self.update()
        return np.random.choice(len(probs), p=probs)


    def policy(self):
        if np.sum(self.acum) == 0:
            return np.ones(self.game.num_actions(self.agent)) / self.game.num_actions(self.agent)
        
        safe_acum = np.maximum(self.acum, 0)
        if np.sum(safe_acum) == 0:
            return np.ones(self.game.num_actions(self.agent)) / self.game.num_actions(self.agent)
        return  safe_acum / np.sum(safe_acum)
    
