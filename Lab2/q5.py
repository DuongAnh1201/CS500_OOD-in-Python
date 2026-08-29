def rectangle_of_symbols(height: int, weight: int, symbol:str) -> None:
    for col in range(height):
        for row in range(weight):
            print(symbol, end = "")
        print()

def main():
    print('Print a rectangle of symbols')
    height = int(input("Enter the height: "))
    weight = int(input("Enter the weight: "))
    symbol = input("Enter the symbol: ")
    rectangle_of_symbols(height, weight, symbol)

if __name__ == "__main__":
    main()