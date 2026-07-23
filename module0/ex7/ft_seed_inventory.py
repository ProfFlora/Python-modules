def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit not in ["packets", "grams", "area"]:
        print("Unknown unit type")
        return
    print(seed_type.capitalize() + " seeds: ", end="")
    if unit == "packets":
        print(quantity, end="")
        print(" packets available")
    if unit == "grams":
        print(quantity, end="")
        print(" grams total")
    if unit == "area":
        print("covers ", end="")
        print(quantity, end="")
        print(" square meters")
