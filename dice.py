"""Dice rolling simulation with frequency visualization."""

import random
import matplotlib.pyplot as plt


def plot_dice_frequency(func):
    """Decorator that plots frequency distribution of dice rolls."""
    def wrapper(count, seed=None):
        if seed is not None:
            random.seed(seed)

        generator = func(count)
        numbers = list(generator)

        frequencies = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for num in numbers:
            frequencies[num] += 1

        percentages = {num: (freq / count) * 100 for num, freq in frequencies.items()}

        plt.figure(figsize=(8, 6))

        bars = plt.bar(frequencies.keys(), percentages.values(), color="skyblue")

        plt.title(f"Dice Roll Percentage Distribution for {count} rolls")
        plt.xlabel("Dice Value")
        plt.ylabel("Percentage (%)")

        plt.ylim(0, 100)
        plt.yticks([0, 20, 40, 60, 80, 100])

        plt.xticks([1, 2, 3, 4, 5, 6])

        for bar in bars:
            height = bar.get_height()
            plt.text(
                bar.get_x() + bar.get_width() / 2.0,
                height + 1,
                f"{height:.1f}%",
                ha="center",
            )

        plt.tight_layout()
        plt.show()

        return (num for num in numbers)

    return wrapper


counts = [10, 100, 1000, 10000, 100000, 500000]


@plot_dice_frequency
def roll_dice(count):
    """Generate random dice rolls."""
    for i in range(count):
        yield random.randint(1, 6)


def run_all_dice_rolls(seed=None):
    """Run dice roll simulations for all count values."""
    for c in counts:
        print(f"Rolling the dice {c} times...")
        _ = roll_dice(c, seed)
        print(f"Completed {c} rolls\n")


seed_input = input("Enter a random seed (or press Enter for no seed): ").strip()
seed = int(seed_input) if seed_input else None

run_all_dice_rolls(seed)