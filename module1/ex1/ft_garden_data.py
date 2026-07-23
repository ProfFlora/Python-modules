class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    plant_one = Plant("Hibiscus", 70, 60)
    plant_two = Plant("Rosemary", 50, 35)
    plant_three = Plant("Corpse Flower", 100, 355)
    print("=== Garden Plant Registry ===")
    plant_one.show()
    plant_two.show()
    plant_three.show()


if __name__ == "__main__":
    main()
