def garden_operations(operation_number: int) -> None:
    a = 1
    match operation_number:
        case 0:
            a = int("abc")
        case 1:
            a = 1/0
        case 2:
            a = open("file_that_doesnt_exist")
        case 3:
            a = "a" + a
        case _:
            return


def test_error_types() -> None:
    print("=== Garden Operations Demo ===")

    for i in (0, 1, 2, 3, 4, 5):
        try:
            print(f"Testing operation {i}...")
            garden_operations(i)
            print("Operation completed successfully")
        except ValueError as error:
            print(f"Caught ValueError: {error}")
        except ZeroDivisionError as error:
            print(f"Caught ZeroDivisionError: {error}")
        except FileNotFoundError as error:
            print(f"Caught FileNotFoundError: {error}")
        except TypeError as error:
            print(f"Caught TypeError: {error}")

    print("\nAll error types tested sucessfully!")


if __name__ == "__main__":
    test_error_types()
