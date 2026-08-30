def rectangle_of_symbols(height: int, weight: int, symbol:str) -> None:
    #For each row 
    for row in range(height):
        # For each column in a row
        for col in range(weight):
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