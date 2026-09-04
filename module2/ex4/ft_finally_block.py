class GardenError(Exception):
    def __init__(self, message: str = "Unknown plant error"):
        self.message = message


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def water_plant(plant_name: str) -> None:

    if plant_name == plant_name.capitalize():
        print(f"Watering {plant_name}: [OK]")
    else:
        raise PlantError(f"Invalid plant name to water: '{plant_name}'")


def test_watering_system() -> None:

    print("=== Garden Watering System ===")

    print("\nTesting valid plants...")
    print("Open watering system")
    try:
        for plant in ["Tomato", "Lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nTesting invalid plants...")
    print("Open watering system")
    try:
        for plant in ["Tomato", "lettuce", "Carrots"]:
            water_plant(plant)
    except PlantError as error:
        print(f"Caught PlantError: {error}")
        print(".. ending tests and returning to main")
    finally:
        print("Closing watering system")

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
