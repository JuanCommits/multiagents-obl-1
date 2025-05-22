import os
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime

def create_results_dir(game_name, config_name=None):
    """Create a structured results directory.
    
    Args:
        game_name (str): Name of the game (e.g., 'foraging', 'blotto')
        config_name (str, optional): Configuration name for the specific experiment setup
    
    Returns:
        str: Path to the created directory
    """
    # Create main results directory if it doesn't exist
    results_dir = os.path.join("results", game_name)
    os.makedirs(results_dir, exist_ok=True)
    
    # If config_name is provided, create a subdirectory for this configuration
    if config_name:
        config_dir = os.path.join(results_dir, config_name)
        os.makedirs(config_dir, exist_ok=True)
        return config_dir
    
    return results_dir

def create_experiment_dir(base_dir, n_agents):
    """Create a directory for a specific experiment run.
    
    Args:
        base_dir (str): Base directory path
        n_agents (int): Number of agents in the experiment
    
    Returns:
        str: Path to the created directory
    """
    experiment_dir = os.path.join(base_dir, f"{n_agents}_agents")
    os.makedirs(experiment_dir, exist_ok=True)
    return experiment_dir

def smooth_data(data, window_size):
    """Apply moving average smoothing to the data."""
    return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

def plot_results(rewards_list, agent_types_list, n_agents, smoothing_window=10, filename=None):
    """Plot experiment results with confidence intervals."""
    plt.figure(figsize=(12, 6))
    
    for rewards, agent_types in zip(rewards_list, agent_types_list):
        # Handle dictionary of rewards
        if isinstance(rewards, dict):
            # Convert dictionary of rewards to a single array by averaging across agents
            rewards_array = np.array([rewards[agent_id] for agent_id in sorted(rewards.keys())])
            rewards = np.mean(rewards_array, axis=0)  # Average across agents
        
        # Calculate mean and std across runs
        mean_rewards = np.mean(rewards, axis=0)
        std_rewards = np.std(rewards, axis=0)
        
        # Smooth the data
        smoothed_mean = smooth_data(mean_rewards, smoothing_window)
        smoothed_std = smooth_data(std_rewards, smoothing_window)
        
        # Plot mean with confidence interval
        x = np.arange(len(smoothed_mean))
        plt.plot(x, smoothed_mean, label=f"{' vs '.join(agent_types)}")
        plt.fill_between(x, 
                        smoothed_mean - smoothed_std,
                        smoothed_mean + smoothed_std,
                        alpha=0.2)
    
    plt.xlabel('Episode')
    plt.ylabel('Average Reward')
    plt.title(f'Foraging Game Results (n={n_agents})')
    plt.legend()
    plt.grid(True)
    
    if filename:
        plt.savefig(filename)
        plt.close()
    else:
        plt.show() 