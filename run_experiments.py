import os
import argparse
from experiments.matrix_game_experiments import run_matrix_game_experiments
from experiments.foraging_experiments import run_foraging_experiments
from experiments.utils import create_results_dir

def main():
    parser = argparse.ArgumentParser(description='Run experiments for matrix games and foraging')
    parser.add_argument('--num_episodes', type=int, default=1000,
                      help='Number of episodes per run')
    parser.add_argument('--num_runs', type=int, default=10,
                      help='Number of runs per experiment')
    parser.add_argument('--matrix_games', action='store_true',
                      help='Run matrix game experiments')
    parser.add_argument('--foraging', action='store_true',
                      help='Run foraging experiments')
    args = parser.parse_args()

    # Create main results directory
    results_dir = create_results_dir("results")
    print(f"Results will be saved in: {results_dir}")

    # Run matrix game experiments if requested
    if args.matrix_games:
        print("\nRunning matrix game experiments...")
        run_matrix_game_experiments(
            n_episodes=args.num_episodes,
            n_runs=args.num_runs
        )

    # Run foraging experiments if requested
    if args.foraging:
        print("\nRunning foraging experiments...")
        run_foraging_experiments(
            n_episodes=args.num_episodes,
            n_runs=args.num_runs
        )

    # If no specific experiment type is specified, run all
    if not (args.matrix_games or args.foraging):
        print("\nRunning all experiments...")
        run_matrix_game_experiments(
            n_episodes=args.num_episodes,
            n_runs=args.num_runs
        )
        run_foraging_experiments(
            n_episodes=args.num_episodes,
            n_runs=args.num_runs
        )

if __name__ == "__main__":
    main() 