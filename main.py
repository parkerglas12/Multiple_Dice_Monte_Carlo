import numpy as np
from numpy.random import PCG64 as pcg
from numpy.random import Generator as gen
import matplotlib.pyplot as plt
import seaborn as sns

def get_user_input() -> int:
    while True:
        try:
            num_dice: int = int(input("How many dice would you like to roll at once (2-4): "))
            sims: int = int(input("How many dice rolls would you like to perform: "))
            if sims <= 1 or sims >= 100000001:
                raise ValueError("Enter an integer between 2 and 100,000,000 for the number of dice rolls.")
            if num_dice <= 1 or num_dice >= 5:
                raise ValueError("Enter an integer between 2 and 4 for dice count.")
        except ValueError as e:
            print(f"Error: {e}")
        else:
            return sims, num_dice 

def get_results(rng, sims: int, num_dice: int) -> dict[int, int]:
    results = rng.integers(1, 7, size=(sims, num_dice)).sum(axis=1)
    unique, counts = np.unique(results, return_counts=True)
    return dict(zip(unique, counts))

def print_results(results: dict[int, int], sims: int) -> None:
    results_string: str = "".join(f"\n{outcome}: {count:,}" for outcome, count in sorted(results.items()))
    print(f"Results of the {sims:,} rolls -> {results_string}")

def create_bar_chart(results: dict[int, int], sims: int, num_dice: int) -> None:
    sns.set()
    sns.set_style("white")
    plt.figure(figsize=(10, 6))

    outcomes: list[int] = sorted(results.keys())
    counts: list[int] = [results[outcome] for outcome in outcomes]

    plt.bar(outcomes, counts, color="#0081cf")
    plt.xlabel("Outcome", fontsize=14, weight="bold", labelpad=10)
    plt.xticks(range(num_dice, num_dice * 6 + 1), fontsize=12, weight="bold")
    plt.ylabel("Count",  fontsize=14, weight="bold", labelpad=15)
    plt.title(f"Monte Carlo Simulation of {sims:,} Rolls with {num_dice} Dice",  fontsize=14, weight="bold", pad=15)

    sns.despine()
    plt.tight_layout(pad=1)
    plt.show()

def main() -> None:
    rng = gen(pcg()) # Random number generator
    sims, num_dice = get_user_input()
    results: dict[int, int] = get_results(rng, sims, num_dice)
    print_results(results , sims)
    create_bar_chart(results, sims, num_dice)

if __name__ == "__main__":
    main()