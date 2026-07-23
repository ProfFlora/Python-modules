def recursive_printer(day: int) -> None:
    if day > 1:
        recursive_printer(day - 1)
    print("Day ", end="")
    print(day)


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    if days >= 1:
        recursive_printer(days)
    print("Harvest time!")
