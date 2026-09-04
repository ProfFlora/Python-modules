class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def plant_error() -> None:
    raise PlantError("The tomato plant is wilting!")


def water_error() -> None:
    raise WaterError("Not enough water in the tank!")


def test_custom_errors() -> None:

    print("=== Custom Garden Errors Demo ===")

    print("\nTesting PlantError...")
    try:
        plant_error()
    except PlantError as error:
        print(f"Caught PlantError: {error}")

    print("\nTesting WaterError...")
    try:
        water_error()
    except WaterError as error:
        print(f"Caught WaterError: {error}")

    print("\nTesting catching all garden errors...")
    for i in (plant_error, water_error):
        try:
            i()
        except GardenError as error:
            print(f"Caught GardenError: {error}")

    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    test_custom_errors()
