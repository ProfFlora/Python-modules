class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name = name
        self.height = height
        self.how_old = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.how_old} days old")

    def grow(self, growth: float = 0.8) -> None:
        self.height = round(self.height + growth, 2)

    def age(self, aging: int = 1) -> None:
        self.how_old += aging


def main() -> None:
    first = Plant("Rose", 8, 2)
    second = Plant("Oak", 500, 13562)
    third = Plant("Carrot", 16, 30)
    fourth = Plant("Mandrake", 35, 62)
    fifth = Plant("The 42 Plant", 42, 42)
    for plant in [first, second, third, fourth, fifth]:
        print("Created: ", end="")
        plant.show()


if __name__ == "__main__":
    main()
