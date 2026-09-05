import sys
import typing


def open_file(file_name: str) -> typing.IO:
    try:
        return open(file_name, "r")
    except OSError as error:
        print(f"Error opening file {file_name}: {error}")
        raise


def read_file(file: typing.IO) -> str:
    try:
        return (file.read())
    except OSError as error:
        print(f"Error reading file: {error}")
        raise


def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
    elif len(sys.argv) > 2:
        print("Please, give me one and only one file name")

    else:
        print("=== Cyber Archives Recovery ===")
        file_opened = False
        file: typing.IO
        try:
            print(f"Accessing file '{sys.argv[1]}'")
            file = open_file(sys.argv[1])
            file_opened = True
            print("---\n")
            print(read_file(file))
            print("\n---")
        except OSError:
            pass
        finally:
            if file_opened:
                file.close()
                print(f"File '{sys.argv[1]}' closed.")


if __name__ == "__main__":
    main()
