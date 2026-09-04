class InputTempError(Exception):
    def __init__(self, message: str):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return f"{self.message}"


def input_temperature(temp_str: str) -> int:
    try:
        temp = int(temp_str)
    except ValueError:
        raise
    if temp < 0:
        raise InputTempError(f"{temp} is too cold for plants (min 0°C)")
    if temp > 40:
        raise InputTempError(f"{temp} is too hot for plants (max 40°C)")
    return temp


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    for string in ("25", "abc", "100", "-50"):
        print(f"Input data is '{string}'")
        try:
            temp = input_temperature(string)
        except ValueError:
            print("Caught input_temperature error: ", end="")
            print(f"invalid literal for int() with base 10: '{string}'\n")
        except InputTempError as error_message:
            print("Caught input_temperature error: ", end="")
            print(error_message, end="\n\n")
        else:
            print(f"Temperature is now {temp}ºC\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
