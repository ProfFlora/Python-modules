def print_info(name: str, height: int, age: int) -> None:
    print("Plant: " + name)
    print(f"Height: {height}cm")
    print(f"Age: {age} days\n")


if __name__ == "__main__":
    name = "Rose"
    height = 25
    age = 30
    print("=== Welcome to My Garden ===")
    print_info(name, height, age)
    print("=== End of Program ===")
