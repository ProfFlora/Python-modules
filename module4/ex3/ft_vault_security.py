def secure_archive(file_name: str, mode: str = "r",
                   string: str = "") -> tuple[bool, str]:
    if mode not in ("r", "w", "a"):
        return (False, "Invalid open mode")

    try:
        with open(file_name, mode) as file:
            if mode == "r":
                return (True, file.read())
            else:
                file.write(string)
                return (True, "Content successfully written to file")
    except OSError as error:
        return (False, f"OSError: {error}")
    except Exception as error:
        return (False, str(error))


def main() -> None:
    print(secure_archive("miau"))
    print(secure_archive("auau"))
    print(secure_archive("auau", "w", "novo texto!!!"))


if __name__ == "__main__":
    main()
