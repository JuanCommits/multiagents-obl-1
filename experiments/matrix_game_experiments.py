import os
import numpy as np
import random
from tqdm.auto import tqdm
from games import MatchingPennies, RockPaperScissors, Blotto
from agents.random_agent import RandomAgent
from agents.fictitiousplay import FictitiousPlay
from agents.regretmatching import RegretMatching
from experiments.utils import create_results_dir, smooth_data
import matplotlib.pyplot as plt
from base.game import SimultaneousGame

def create_agents(game: SimultaneousGame, agent_types: list, seed: int):
    """Create agents based on the specified types."""
    agents = []
    for i, agent_id in enumerate(game.agents):
        agent_type = agent_types[game.agent_name_mapping[agent_id]]
        if agent_type == "random":
            agents.append(RandomAgent(game, agent_id, seed=seed + i))
        elif agent_type == "fp":
            agents.append(FictitiousPlay(game, agent_id, seed=seed + i))
        elif agent_type == "rm":
            agents.append(RegretMatching(game, agent_id, seed=seed + i))
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
    return agents

def run_experiment(game: SimultaneousGame, agent_types: list, n_episodes: int, n_runs: int, seed: int =79):
    """Run a single experiment with specified agent types."""
    print(f"\nRunning experiment with agents: {agent_types}")
    
    # Set seeds for reproducibility
    np.random.seed(seed)
    random.seed(seed)
    
    # Initialize results for this run
    run_rewards = {agent_id: np.zeros((n_runs, n_episodes)) for agent_id in game.agents}
    run_actions = {agent_id: np.zeros((n_runs, n_episodes)) for agent_id in game.agents}
    
    # Run multiple times
    for run in tqdm(range(n_runs), desc="Runs", leave=True):
        # Create fresh agents for each run with different seeds
        run_seed = seed + run
        agents = create_agents(game, agent_types, run_seed)
        
        # Run episodes
        for episode in tqdm(range(n_episodes), desc=f"Run {run+1}", leave=False):
            # Get actions from all agents
            actions = {agent.agent: agent.action() for agent in agents}
            
            # Step the environment
            game.step(actions)
            
            # Store results for each agent
            for agent_id in game.agents:
                agent_reward = game.reward(agent_id)
                run_rewards[agent_id][run, episode] = agent_reward
                run_actions[agent_id][run, episode] = actions[agent_id]
            
            # Update agents
            for agent in agents:
                agent.update()
    
    return {
        'rewards': run_rewards,
        'actions': run_actions
    }

def plot_experiment_results(results, agent_types, n_agents, smoothing_window=10, filename=None):
    """Plot all experiment results in a single figure with subplots."""
    fig = plt.figure(figsize=(15, 20))
    gs = fig.add_gridspec(4, 2)
    
    # Plot 1: Instantaneous Rewards
    ax1 = fig.add_subplot(gs[0, :])
    for agent_id, rewards in results['rewards'].items():
        # Calculate mean and std across runs
        mean_rewards = np.mean(rewards, axis=0)
        std_rewards = np.std(rewards, axis=0)
        
        # Smooth the data
        smoothed_mean = smooth_data(mean_rewards, smoothing_window)
        smoothed_std = smooth_data(std_rewards, smoothing_window)
        
        # Plot mean with confidence interval
        x = np.arange(len(smoothed_mean))
        agent_idx = int(agent_id.split('_')[1])
        ax1.plot(x, smoothed_mean, label=f"Agent {agent_idx} ({agent_types[agent_idx]})")
        ax1.fill_between(x, 
                        smoothed_mean - smoothed_std,
                        smoothed_mean + smoothed_std,
                        alpha=0.2)
    
    ax1.set_xlabel('Episode')
    ax1.set_ylabel('Reward')
    ax1.set_title('Instantaneous Rewards')
    ax1.legend()
    ax1.grid(True)
    
    # Plot 2: Cumulative Rewards
    ax2 = fig.add_subplot(gs[1, :])
    for agent_id, rewards in results['rewards'].items():
        # Calculate cumulative rewards
        cumulative_rewards = np.cumsum(rewards, axis=1)
        mean_cumulative = np.mean(cumulative_rewards, axis=0)
        std_cumulative = np.std(cumulative_rewards, axis=0)
        
        # Smooth the data
        smoothed_mean = smooth_data(mean_cumulative, smoothing_window)
        smoothed_std = smooth_data(std_cumulative, smoothing_window)
        
        x = np.arange(len(smoothed_mean))
        agent_idx = int(agent_id.split('_')[1])
        ax2.plot(x, smoothed_mean, label=f"Agent {agent_idx} ({agent_types[agent_idx]})")
        ax2.fill_between(x, 
                        smoothed_mean - smoothed_std,
                        smoothed_mean + smoothed_std,
                        alpha=0.2)
    
    ax2.set_xlabel('Episode')
    ax2.set_ylabel('Cumulative Reward')
    ax2.set_title('Cumulative Rewards')
    ax2.legend()
    ax2.grid(True)
    
    # Plot 3: Actions over time
    ax3 = fig.add_subplot(gs[2, :])
    for agent_id, actions in results['actions'].items():
        # Calculate mean and std across runs
        mean_actions = np.mean(actions, axis=0)
        std_actions = np.std(actions, axis=0)
        
        # Smooth the data
        smoothed_mean = smooth_data(mean_actions, smoothing_window)
        smoothed_std = smooth_data(std_actions, smoothing_window)
        
        x = np.arange(len(smoothed_mean))
        agent_idx = int(agent_id.split('_')[1])
        ax3.plot(x, smoothed_mean, label=f"Agent {agent_idx} ({agent_types[agent_idx]})")
        ax3.fill_between(x, 
                        smoothed_mean - smoothed_std,
                        smoothed_mean + smoothed_std,
                        alpha=0.2)
    
    ax3.set_xlabel('Episode')
    ax3.set_ylabel('Action')
    ax3.set_title('Actions Over Time')
    ax3.legend()
    ax3.grid(True)
    
    # Plot 4: Action Distribution Histograms
    ax4 = fig.add_subplot(gs[3, 0])
    for agent_id, actions in results['actions'].items():
        # Flatten actions across all runs and episodes
        flat_actions = actions.flatten()
        agent_idx = int(agent_id.split('_')[1])
        
        # Create histogram
        ax4.hist(flat_actions, alpha=0.5, label=f"Agent {agent_idx} ({agent_types[agent_idx]})",
                bins=20, density=True)
    
    ax4.set_xlabel('Action')
    ax4.set_ylabel('Frequency')
    ax4.set_title('Action Distribution')
    ax4.legend()
    ax4.grid(True)
    
    # Plot 5: Win Rate over time
    ax5 = fig.add_subplot(gs[3, 1])
    for agent_id, rewards in results['rewards'].items():
        # Calculate win rate (episodes where reward > 0)
        wins = (rewards > 0).astype(float)
        win_rate = np.mean(wins, axis=0)
        
        # Smooth the data
        smoothed_win_rate = smooth_data(win_rate, smoothing_window)
        
        x = np.arange(len(smoothed_win_rate))
        agent_idx = int(agent_id.split('_')[1])
        ax5.plot(x, smoothed_win_rate, label=f"Agent {agent_idx} ({agent_types[agent_idx]})")
    
    ax5.set_xlabel('Episode')
    ax5.set_ylabel('Win Rate')
    ax5.set_title('Win Rate Over Time')
    ax5.legend()
    ax5.grid(True)
    
    # Adjust layout and save/show
    plt.tight_layout()
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()

def run_matrix_game_experiments(n_episodes=1000, n_runs=10):
    """Run matrix game experiments."""
    # Create results directory
    results_dir = create_results_dir("matrix_games")
    
    # Define games and their agent combinations
    games = {
        "matching_pennies": MatchingPennies(),
        "rock_paper_scissors": RockPaperScissors(),
        "blotto10-3": Blotto(10, 3),
        "blotto15-5": Blotto(15, 5)

    }
    
    agent_combinations = [
        ["fp", "fp"],
        ["fp", "random"],
        ["fp", "rm"],
        ["rm", "random"],
        ["rm", "rm"],
    ]
    
    # Run experiments for each game
    for game_name, game in games.items():
        print(f"\nRunning experiments for {game_name}")
        
        # Create directory for this game
        game_dir = os.path.join(results_dir, game_name)
        os.makedirs(game_dir, exist_ok=True)
        
        # Run each agent combination
        for agent_types in agent_combinations:
            # Run experiment
            results = run_experiment(game, agent_types, n_episodes, n_runs)
            
            # Save combined plot for this combination
            agent_str = '_vs_'.join(agent_types)
            filename = os.path.join(game_dir, f"experiment_results_{agent_str}.png")
            plot_experiment_results(results, agent_types, len(agent_types), filename=filename)
            print(f"Results saved to {filename}")
    
    print(f"\nAll results saved in: {results_dir}")

if __name__ == "__main__":
    run_matrix_game_experiments() 