import sys


def main() -> None:

    n = len(sys.argv)
    print("=== Command Quest ===")

    print(f"Program name: {sys.argv[0]}")
    if n == 1:
        print("No arguments provided!")
    else:
        iter = 1
        try:
            while iter < n:
                print(f"Argment {iter}: {sys.argv[iter]}")
                iter += 1
        except IndexError as error:
            print(f"Caught IndexError: {error}")

    print(f"Total arguments: {n}")


if __name__ == "__main__":
    main()
