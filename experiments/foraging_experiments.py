import os
import numpy as np
from tqdm.auto import tqdm
from games.foraging import Foraging as ForagingGame
from agents.random_agent import RandomAgent
from agents import QLearningAgent, JointActionLearningActionModelling
from experiments.utils import create_results_dir, plot_results, create_experiment_dir, smooth_data
from base.game import SimultaneousGame
from base.agent import Agent
import matplotlib.pyplot as plt
import random

def create_agents(game: SimultaneousGame, agent_types: list[str], seed: int = 42) -> list[Agent]:
    """Create agents based on the specified types."""
    agents = []
    for i, agent_id in enumerate(game.agents):
        agent_type = agent_types[game.agent_name_mapping[agent_id]]
        if agent_type == "random":
            agents.append(RandomAgent(game, agent_id))
        elif agent_type == "iql":
            agents.append(QLearningAgent(
                game,
                agent_id,
                learning_rate=0.1,
                discount_factor=0.9,
                exploration_prob=1.0,
                exploration_decay=0.9999,
                min_epsilon=0.1,
                seed=seed + i
            ))
        elif agent_type == "jal-am":
            agents.append(JointActionLearningActionModelling(
                game,
                agent_id,
                learning_rate=0.1,
                discount_factor=0.9,
                exploration_prob=1.0,
                exploration_decay=0.9999,
                min_epsilon=0.1,
                seed=seed + i
            ))
        else:
            raise ValueError(f"Unknown agent type: {agent_type}")
    return agents

def run_experiment(game, agent_types, n_episodes, n_runs, seed=79):
    """Run a single experiment with specified agent types."""
    print(f"\nRunning experiment with agents: {agent_types}")

    if len(agent_types) == 3:
        n_episodes *= 2
        n_runs = n_runs // 2
    
    # Set seeds for reproducibility
    np.random.seed(seed)
    random.seed(seed)
    
    # Initialize results for this run
    run_rewards = {agent_id: np.zeros((n_runs, n_episodes)) for agent_id in game.agents}
    run_actions = np.zeros((n_runs, n_episodes, len(agent_types)))
    run_food_collected = np.zeros((n_runs, n_episodes))  # Track food collected per episode
    run_steps_to_food = np.zeros((n_runs, n_episodes))   # Track steps needed to collect food
    
    # Run multiple times
    for run in tqdm(range(n_runs), desc="Runs", leave=True):
        # Create fresh agents for each run with different seeds
        run_seed = seed + run
        agents = create_agents(game, agent_types, run_seed)
            
        # Run episodes
        for episode in tqdm(range(n_episodes), desc=f"Run {run+1}", leave=False):
            # Get actions from all agents
            episode_food_collected = 0
            steps_done = 0
            game.reset(seed=seed + episode)
            while not game.done():
                actions = {agent.agent: agent.action() for agent in agents}
                
                # Step the environment
                game.step(actions)
                steps_done += 1
                
                # Update agents
                for agent in agents:
                    agent.update()
                
                # Store results
                for agent_id in game.agents:
                    reward = game.reward(agent_id)
                    run_rewards[agent_id][run, episode] += reward
                    if reward > 0:  # Positive reward indicates food collection
                        episode_food_collected += 1
            
            run_actions[run, episode] = [actions[agent.agent] for agent in agents]
            
            # Track food collection
            run_food_collected[run, episode] = episode_food_collected
            
            # Track steps to food
            if episode_food_collected > 0:
                run_steps_to_food[run, episode] = steps_done
    
    return {
        'rewards': run_rewards,
        'actions': run_actions,
        'food_collected': run_food_collected,
        'steps_to_food': run_steps_to_food
    }

def plot_experiment_results(results, agent_types, n_agents, smoothing_window=10, filename=None):
    """Plot all experiment results in a single figure with subplots."""
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(12, 15))
    
    # Plot 1: Rewards
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
    ax1.set_title(f'Agent Rewards (n={n_agents})')
    ax1.legend()
    ax1.grid(True)
    
    # Plot 2: Food Collection
    mean_food = np.mean(results['food_collected'], axis=0)
    std_food = np.std(results['food_collected'], axis=0)
    
    # Smooth the data
    smoothed_mean = smooth_data(mean_food, smoothing_window)
    smoothed_std = smooth_data(std_food, smoothing_window)
    
    # Plot mean with confidence interval
    x = np.arange(len(smoothed_mean))
    ax2.plot(x, smoothed_mean, label='Food Collected')
    ax2.fill_between(x, 
                    smoothed_mean - smoothed_std,
                    smoothed_mean + smoothed_std,
                    alpha=0.2)
    
    ax2.set_xlabel('Episode')
    ax2.set_ylabel('Food Collected')
    ax2.set_title('Food Collection Rate')
    ax2.legend()
    ax2.grid(True)
    
    # Plot 3: Steps to Food
    mean_steps = np.mean(results['steps_to_food'], axis=0)
    std_steps = np.std(results['steps_to_food'], axis=0)
    
    # Smooth the data
    smoothed_mean = smooth_data(mean_steps, smoothing_window)
    smoothed_std = smooth_data(std_steps, smoothing_window)
    
    # Plot mean with confidence interval
    x = np.arange(len(smoothed_mean))
    ax3.plot(x, smoothed_mean, label='Steps to Food')
    ax3.fill_between(x, 
                    smoothed_mean - smoothed_std,
                    smoothed_mean + smoothed_std,
                    alpha=0.2)
    
    ax3.set_xlabel('Episode')
    ax3.set_ylabel('Steps to Collect Food')
    ax3.set_title('Steps Required to Collect Food')
    ax3.legend()
    ax3.grid(True)
    
    # Adjust layout and save/show
    plt.tight_layout()
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show()

def run_foraging_experiments(n_agents_list=[2, 3], grid_sizes=[6, 8], numbers_fruits=[1, 2, 3], n_episodes=5000, n_runs=10):
    """Run foraging experiments with different numbers of agents."""
    # Define agent combinations to test
    agent_combinations = [
        ["iql", "iql"],
        ["iql", "jal-am"],
        ["jal-am", "jal-am"]
    ]
    
    # Run experiments for each number of agents
    for grid_size in grid_sizes:
        for number_fruits in numbers_fruits:
            for n_agents in n_agents_list:
                print(f"\nRunning experiments with {n_agents} agents")
                
                # Create game instance
                config = f"Foraging-{grid_size}x{grid_size}-{n_agents}p-{number_fruits}f-v3"
                game = ForagingGame(config=config, seed=42)
                
                # Create configuration directory
                config_name = f"grid{grid_size}x{grid_size}_fruits{number_fruits}"
                config_dir = create_results_dir("foraging", config_name)
                
                # Create experiment directory for this run
                experiment_dir = create_experiment_dir(config_dir, n_agents)
                
                # Store results for plotting
                all_rewards = []
                all_agent_types = []
                
                # Run each agent combination
                for agent_types in agent_combinations:
                    # Extend agent types list to match number of agents
                    extended_types = agent_types * (n_agents // len(agent_types))
                    if n_agents % len(agent_types) != 0:
                        extended_types.extend(agent_types[:n_agents % len(agent_types)])
                    
                    # Run experiment
                    results = run_experiment(game, extended_types, n_episodes, n_runs)
                    
                    # Store results
                    all_rewards.append(results['rewards'])
                    all_agent_types.append(extended_types)
                    
                    # Save combined plot for this combination
                    agent_str = '_vs_'.join(extended_types)
                    filename = os.path.join(experiment_dir, f"experiment_results_{n_agents}agents_{agent_str}.png")
                    plot_experiment_results(results, extended_types, n_agents, filename=filename)
                    print(f"Results saved to {filename}")
        
    print(f"\nAll results saved in: results/foraging/")

if __name__ == "__main__":
    run_foraging_experiments() 