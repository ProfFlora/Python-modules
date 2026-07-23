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
    plant = Plant("Rose", 25.0, 30)
    starting_height = plant.height
    print("=== Garden Plant Growth ===")
    plant.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        plant.age()
        plant.grow()
        plant.show()
    print(f"Growth this week: {round(plant.height - starting_height, 2)}cm")


if __name__ == "__main__":
    main()
