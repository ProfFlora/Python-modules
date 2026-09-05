import sys


def inventory_parser(items: list) -> dict:
    inventory: dict = {}
    for item in items:
        pair = item.split(':')
        if len(pair) != 2:
            print(f"Error - invalid parameter '{item}'")
        elif pair[0] in inventory.keys():
            print(f"Redundant item '{pair[0]}' - discarding")
        else:
            try:
                value = int(pair[1])
                if value <= 0:
                    print(f"Invalid quantity for {pair[0]}: {value}")
                else:
                    inventory[pair[0]] = value
            except ValueError as error:
                print(f"Quantity error for '{pair[0]}: {error}")

    return inventory


def inventory_max(inventory: dict) -> str:
    max_key = None
    max_value = 0
    for item in inventory.keys():
        if inventory[item] > max_value:
            max_key = item
            max_value = inventory[item]

    return max_key


def inventory_min(inventory: dict) -> str:
    min_key = None
    min_value = 0
    for item in inventory.keys():
        if inventory[item] < min_value or min_value == 0:
            min_key = item
            min_value = inventory[item]

    return min_key


def inventory_show(inventory: dict) -> None:
    print(f"Got inventory: {inventory}")
    print(f"Item list: {inventory.keys()}")

    total = sum(inventory.values())
    print(f"Total quantity of the {len(inventory)} items: {total}")
    for item in inventory.keys():
        print(f"Item {item} represents ", end='')
        print(f"{round((inventory[item] * 100) / total, 1)}%")

    max = inventory_max(inventory)
    print(f"Item most abundant: {max} with quantity {inventory[max]}")
    min = inventory_min(inventory)
    print(f"Item least abundant: {min} with quantity {inventory[min]}")

    inventory.update({"Pocket Sand": 50})
    print(f"Updated inventory: {inventory}")


def main() -> None:
    print("=== Inventory System Analysis ===")
    inventory = inventory_parser(sys.argv[1:])
    inventory_show(inventory)


if __name__ == "__main__":
    main()
