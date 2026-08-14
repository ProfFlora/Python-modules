def input_temperature(temp_str: str) -> int:
    return int(temp_str)


def test_temperature() -> None:
    print("=== Garden Temperature ===\n")
    for string in ("25", "abc"):
        print(f"Input data is '{string}'")
        try:
            temp = input_temperature(string)
        except ValueError:
            print("Caught input_temperature error: ", end="")
            print("invalid literal for int() with base 10: '{string}'\n")
        else:
            print(f"Temperature is now {temp}ºC\n")
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature()
