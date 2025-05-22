import copy
from pettingzoo.utils import env
from pettingzoo.utils.env import ParallelEnv

ObsDict = env.ObsDict
AgentID = env.AgentID
ActionDict = env.ActionDict

class SimultaneousGame(ParallelEnv):

    observations: ObsDict
    rewards: dict[AgentID, float]
    terminations: dict[AgentID, bool]
    truncations: dict[AgentID, bool]
    infos: dict[AgentID, dict]

    agent_name_mapping: dict[AgentID, int]

    def observation_space(self, agent: AgentID):
        return self.observation_spaces[agent]

    def action_space(self, agent: AgentID):
        return self.action_spaces[agent]

    def num_actions(self, agent: AgentID):
        return self.action_space(agent).n
    
    def action_iter(self, agent: AgentID):
        return range(self.action_space(agent).start, self.action_space(agent).n)
        
    def observe(self, agent: AgentID):
        return self.observations[agent]
    
    def reward(self, agent: AgentID):
        return self.rewards[agent]
    
    def clone(self):
        game = copy.deepcopy(self)
        game.reset()
        return game
    
    # Added functions
    def has_ended(self, agent: AgentID) -> bool:
        return self.terminations[agent] or self.truncations[agent]

    def observe_action(self, agent: AgentID):
        # A template definition for environments that do not have a specific action observation
        return self.observe(agent)