import math


type Coordinate = tuple[float, float, float]


def get_player_pos() -> Coordinate:

    while True:
        coords = input("Enter new coordinates as floats in format 'x,y,z': ")
        if coords.count(',') != 2:
            print("Invalid syntax")
        else:
            split = coords.split(',', 2)
            parsed: list = [0, 0, 0]
            for i in (0, 1, 2):
                try:
                    parsed[i] = float(split[i])
                except ValueError as error:
                    print(f"Error on parameter {split[i]}: {error}")
                else:
                    if i == 2:
                        return parsed[0], parsed[1], parsed[2]


def get_distance(a: Coordinate, b: Coordinate) -> float:
    sum = 0.0
    for i in (0, 1, 2):
        sum += (a[i] - b[i]) ** 2
    return round(math.sqrt(sum), 4)


def main() -> None:
    print("=== Game Coordinate System ===")

    print("\nGet a first set of coordinates")
    coord1 = get_player_pos()
    print(f"Got a first tuple: {coord1}")
    print(f"It includes X={coord1[0]}, Y={coord1[1]}, Z={coord1[2]}")

    print("\nGet a second set of coordinates")
    coord2 = get_player_pos()

    print("The distance between the 2 sets of coordinates: ", end="")
    print(get_distance(coord1, coord2))


if __name__ == "__main__":
    main()
