class Plant:
    @staticmethod
    def year_check(age: int) -> bool:
        return age > 365

    @classmethod
    def anon(cls) -> Plant:
        return cls(None, 0, 0)

    class Stats:
        def __init__(self) -> None:
            self._grow = 0
            self._ages = 0
            self._show = 0

        def display(self) -> None:
            print("Stats: ", end="")
            print(f"{self._grow} grow, {self._ages} age, {self._show} show")

    def get_stats(self) -> Stats:
        return self._stats

    def get_name(self) -> str:
        if self._name is not None:
            return (self._name)
        else:
            return "Unknown plant"

    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self.name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self.name}: Error, age can't be negative")
            print("Age update rejected")

    def set_growth_factor(self, growth_factor: float) -> None:
        self._growth_factor = growth_factor

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def get_growth_factor(self) -> float:
        return self._growth_factor

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)
        self._growth_factor = 0
        self._stats = self.Stats()

    def show(self) -> None:
        self._stats._show += 1
        print(f"{self._name}: ", end="")
        print(f"{round(self._height, 1)}cm, {self._age} days old")

    def grow(self, growth: float, time: int = 1) -> None:
        self._stats._grow += 1
        self._height += growth * time

    def age(self, aging: int = 1) -> None:
        self._stats._ages += 1
        self._age += aging
        self.grow(self._growth_factor, aging)


class Flower(Plant):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._has_bloomed = False

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        if self._has_bloomed:
            print(f"{self._name} is blooming beautifully!")
        else:
            print(f"{self._name} has not bloomed yet")

    def bloom(self) -> None:
        self._has_bloomed = True


class Seed(Flower):
    def __init__(self, name: str, height: float, age: int, color: str) -> None:
        super().__init__(name, height, age, color)
        if self._has_bloomed:
            self._seeds = 42
        else:
            self._seeds = 0

    def bloom(self) -> None:
        super().bloom()
        self._seed = 42

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")


class Vegetable(Plant):
    def __init__(self, name: str, size: float, age: int, season: str) -> None:
        super().__init__(name, size, age)
        self._season = season
        self._nutritional_value = 0
        self._nutri_rate = 1

    def set_nutritional_value(self, value: int) -> None:
        self._nutritional_value = value

    def set_nutri_rate(self, rate: int) -> None:
        self._nutri_rate = rate

    def get_nutritional_value(self) -> int:
        return self._nutritional_value

    def get_nutri_rate(self) -> int:
        return self._nutri_rate

    def grow(self, growth: float, time: int = 1) -> None:
        super().grow(growth, time)
        self._nutritional_value += self._nutri_rate * time

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._season}")
        print(f"Nutritional value: {self._nutritional_value}")


class Tree(Plant):
    class Stats(Plant.Stats):
        def __init__(self) -> None:
            super().__init__()
            self._shade = 0

        def display(self) -> None:
            super().display()
            print(f"{self._shade} shade")

    def __init__(self, name: str, size: float, age: int, trunk: float) -> None:
        super().__init__(name, size, age)
        self._trunk_diameter = trunk

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")

    def produce_shade(self) -> None:
        self._stats._shade += 1
        print(f"{self._name} now produces a shade", end=" ")
        print(f"{self._height}cm tall and {self._trunk_diameter}cm wide.")


def show_stats(plant: Plant) -> None:
    print(f"[statistics for {plant.get_name()}]")
    plant.get_stats().display()


if __name__ == "__main__":
    print("=== Garden Statistics ===")
    print("=== Check year-old")
    for i in [30, 400]:
        print(f"is {i} days more than a year? -> {Plant.year_check(i)}")

    rose = Flower("Rose", 15.0, 10, "red")
    oak = Tree("Oak", 200.0, 365, 5.0)
    tomato = Vegetable("Tomato", 5.0, 10, "April")
    sunflower = Seed("Sunflower", 80.0, 45, "yellow")

    print("\n=== Flower")
    rose.show()
    show_stats(rose)
    print("[asking the rose to grow and bloom]")
    rose.grow(8, 1)
    rose.bloom()
    rose.show()
    show_stats(rose)

    print("\n=== Tree")
    oak.show()
    show_stats(oak)
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    show_stats(oak)

    print("\n=== Vegetable")
    tomato.show()
    show_stats(tomato)
    print("[make the tomato grow and age for 20 days]")
    tomato.set_growth_factor(2.1)
    tomato.age(20)
    tomato.show()
    show_stats(tomato)

    print("\n=== Seed")
    sunflower.show()
    show_stats(sunflower)
    print("[make sunflower grow, age and bloom]")
    sunflower.set_growth_factor(1.5)
    sunflower.age(20)
    sunflower.bloom()
    sunflower.show()
    show_stats(sunflower)

    print("\n=== Anonymous")
    uk = Plant.anon()
    uk.show()
    show_stats(uk)
