def triangle_of_symbols(height: int, symbol: str = "*") -> None:
    for row in range(height):
        spaces = " " * (height - row - 1)
        symbols = symbol * (2 * row + 1)
        print(spaces + symbols)


def main() -> None:
    print("Print a triangle of symbols")

    height = int(input("Enter the height: "))
    symbol = input("Enter the symbol: ")

    triangle_of_symbols(height, symbol)


if __name__ == "__main__":
    main()