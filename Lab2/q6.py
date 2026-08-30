'''
    printing out a triangle with size of height and with chosen symbol
'''
def triangle_of_symbols(height: int, symbol: str = "*") -> None:
    #For each row in range of height
    for row in range(height):
        #The space before the first symbol
        spaces = " " * (height - row - 1)
        #Number of symbol in the row
        symbols = symbol * (2 * row + 1)
        print(spaces + symbols)


def main() -> None:
    print("Print a triangle of symbols")

    height = int(input("Enter the height: "))
    symbol = input("Enter the symbol: ")

    triangle_of_symbols(height, symbol)


if __name__ == "__main__":
    main()