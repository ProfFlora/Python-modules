import random


def gen_player_achievements(get_all: bool = False) -> set:
    all_acvs = ["Cowabummer",
                "Throne of the Gods",
                "Atonement",
                "C'est la vie...",
                "Chimera Charmer",
                "The Journey Ends Here",
                "Hit the Road, Jack",
                "Not alone in this",
                "AAAAAAAAAAAAAAAAAAAAAAAAAAAA",
                "BBBBBBBBBBBBBBBBBBBBBBBBBBBB",
                "Jogging your Memory",
                "Aw, dangit",
                "Across Time and Space",
                "Diva",
                "Kill him, now!",
                "Farewell",
                "!!!",
                "Come here kittyyyyy",
                "Faring not so well",
                "Mary had a Little Sacrificial Lamb"]
    if get_all:
        return set(all_acvs)
    size = len(all_acvs)
    n = random.binomialvariate(size, 0.45)
    return set(random.sample(all_acvs, n))


def achievment_tracker() -> None:
    print("=== Achievment Tracker System ===")

    sets: dict = {}
    common: set = gen_player_achievements(get_all=True)
    all: set = set()
    for name in ("Alice", "Bob", "Charlie", "Dylan"):
        sets[name] = gen_player_achievements()
        print(f"\nPlayer {name}: {sets[name]}")
        common = common.intersection(sets[name])
        all = all.union(sets[name])

    print(f"\nAll distinct achievement: {all}")
    print(f"\nCommon achievments: {common}")

    for name in ("Alice", "Bob", "Charlie", "Dylan"):
        only: set = sets[name]
        for i in ("Alice", "Bob", "Charlie", "Dylan"):
            if i != name:
                only = only.difference(sets[i])
        print(f"\nOnly {name} has: {only}")

    for name in ("Alice", "Bob", "Charlie", "Dylan"):
        missing = gen_player_achievements(get_all=True).difference(sets[name])
        print(f"\n{name} is missing: {missing}")


if __name__ == "__main__":
    achievment_tracker()
