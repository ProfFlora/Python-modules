class Plant:
    def set_height(self, height: float) -> None:
        if height >= 0:
            self._height = height
        else:
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")

    def set_age(self, age: int) -> None:
        if age >= 0:
            self._age = age
        else:
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def __init__(self, name: str, height: float, age: int) -> None:
        self._name = name
        self._height = 0
        self.set_height(height)
        self._age = 0
        self.set_age(age)

    def show(self) -> None:
        print(f"{self._name}: {self._height}cm, {self._age} days old")

    def grow(self, growth: float = 0.8) -> None:
        self.height = round(self._height + growth, 2)

    def age(self, aging: int = 1) -> None:
        self._age += aging
