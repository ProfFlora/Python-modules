import sys
import typing


def open_file(file_name: str, mode: str = "r") -> typing.IO:
    try:
        return open(file_name, mode)
    except OSError as error:
        print(f"Error opening file '{file_name}': {error}")
        raise


def read_file(file: typing.IO) -> str:
    try:
        return (file.read())
    except OSError as error:
        print(f"Error reading file: {error}")
        raise


def write_file(file: typing.IO, string: str) -> None:
    try:
        file.write(string)
    except OSError as error:
        print(f"Error writing file: {error}")
        raise


def formatted_print(string: str) -> None:
    print("---\n")
    print(string)
    print("\n---")


def main() -> None:

    if len(sys.argv) < 2:
        print("Usage: ft_ancient_text.py <file>")
        return
    elif len(sys.argv) > 2:
        print("Please, give me one and only one file name")
        return

    print("=== Cyber Archives Recovery & Preservation ===")
    file_name = sys.argv[1]
    file_open = False
    file: typing.IO
    file_text: str
    try:
        print(f"Accessing file '{file_name}'")
        file = open_file(file_name)
        file_open = True
        file_text = read_file(file)
    except OSError:
        return
    finally:
        if file_open:
            file.close()
            file_open = False
            print(f"File '{file_name}' closed.")

    formatted_print(file_text)
    print("Transform data:")
    new_text = '\n'.join([line+'#' for line in file_text.split("\n")])
    formatted_print(new_text)

    file_name = input("Enter new file name (or empty): ")
    if file_name == "":
        return

    file_open = False
    try:
        print(f"Saving data to '{file_name}")
        file = open_file(file_name, "w")
        file_open = True
        write_file(file, new_text)
        print(f"Data saved in file '{file_name}")
    except OSError:
        pass
    finally:
        if file_open:
            file.close()
            file_open = False
            print(f"File '{file_name}' closed.")


if __name__ == "__main__":
    main()
