import random


def alchemist() -> None:
    player_names = ["Alice", "bob", "Charlie", "dylan", "Ethan", "Flora",
                    "Gunther", "helga", "ian", "Jax", "kaine", "liam"]
    all_caps = [name.capitalize() for name in player_names]
    only_caps = [name for name in player_names if name == name.capitalize()]
    scores = {name: random.randrange(0, 1000) for name in all_caps}
    avg = round(sum([scores[name] for name in all_caps]) / len(all_caps), 2)
    best_scores = {name: scores[name] for name in all_caps
                   if scores[name] > avg}

    print("=== Game Data Alchemist ===")
    print(f"\nInitial list of players: {player_names}")
    print(f"New list with all names capitalized: {all_caps}")
    print(f"New list of capitalized names only: {only_caps}")
    print(f"\nScore dict: {scores}")
    print(f"Score average is {avg}")
    print(f"High scores: {best_scores}")


if __name__ == "__main__":
    alchemist()
