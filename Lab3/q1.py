def decima_to_hex(n: int) -> str:
    '''
    The function convert the decimal numbers to hexagon format
    '''
    hex_digits = "0123456789ABCDEF"
    hex_value = ""

    

    if n == 0:
        hex_value = "0"
    else:
        while n > 0:
            remainder = n % 16
            hex_value = hex_digits[remainder] + hex_value
            n = n // 16

    return hex_value

def main():
    number = int(input("Enter a decimal value: "))
    print(f"The hex value is: {decima_to_hex(number)}")

if __name__ == "__main__":
    main()
    