import random
import matplotlib.pyplot as plt
from tabulate import tabulate


def roll_dice():
    return random.randint(1, 6)


def monte_carlo_simulation(num_simulations):
    results = {i: 0 for i in range(2, 13)}

    for _ in range(num_simulations):
        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2
        results[total] += 1

    probabilities = {key: value / num_simulations for key, value in results.items()}
    return probabilities


def plot_probabilities(probabilities):
    plt.bar(probabilities.keys(), probabilities.values())
    plt.title('Monte Carlo Simulation: Probability of Each Sum')
    plt.xlabel('Sum of Dice')
    plt.ylabel('Probability')
    plt.show()


def main():
    num_simulations = 1000_000
    probabilities = monte_carlo_simulation(num_simulations)

    plot_probabilities(probabilities)

    table_data = [(key, value) for key, value in probabilities.items()]
    headers = ["Sum", "Probability"]
    print(tabulate(table_data, headers=headers, floatfmt=".4f", tablefmt="fancy_grid"))


if __name__ == "__main__":
    main()
