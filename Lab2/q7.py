def circle_of_symbols(radius: int, symbol: str) -> None:
    diameter = 2 * radius - 1
    edge_rows = radius // 2

    # The Increasing phase of the circle
    for row in range(edge_rows):
        spaces = edge_rows - row
        symbols = diameter - 2 * spaces
        print("  " * spaces + (symbol + " ") * symbols)

    # The stable phase of the circle
    # Number of rows having full symbols
    middle_rows = diameter - 2 * edge_rows
    for _ in range(middle_rows):
        print((symbol + " ") * diameter)

    # The Decreasing phase of the circle
    for row in range(edge_rows - 1, -1, -1):
        spaces = edge_rows - row
        symbols = diameter - 2 * spaces
        print("  " * spaces + (symbol + " ") * symbols)


def main() -> None:
    radius = int(input("Please enter the radius of the circle: "))
    symbol = input("Please enter the symbol character: ")

    circle_of_symbols(radius, symbol)


if __name__ == "__main__":
    main()