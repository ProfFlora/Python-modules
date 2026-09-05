import random
from typing import Generator


def gen_event() -> Generator[tuple[str, str], None, None]:
    players = ["Alice", "Bob", "Charlie", "Dylan", "Ethan", "Flora", "Gunther",
               "Helga", "Ian", "Jax", "Kaine"]
    actions = ["eat", "sleep", "game", "repeat", "swim", "run", "climb",
               "move", "grab", "release"]
    while True:
        yield random.choice(players), random.choice(actions)


def consume_event(event_list: list) -> Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        index = random.randrange(0, len(event_list))
        item = event_list[index]
        event_list[:] = event_list[:index] + event_list[index + 1:]
        yield item


def main() -> None:
    generator = gen_event()

    for i in range(1000):
        player, action = next(generator)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = [next(gen_event()) for i in range(10)]
    print(f"Built list of 10 events: {event_list}")

    for item in consume_event(event_list):
        print(f"Got event from list: {item}")
        print(f"Remains in list: {event_list}")


if __name__ == "__main__":
    main()
