def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for day in range(1, days + 1):
        print("Day ", end="")
        print(day)
    print("Harvest time!")
