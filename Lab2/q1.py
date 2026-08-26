"""
A simple calculator
Input: Get two numbers and the operation
Do the operation and return the result
"""
def add(a:float,b:float) ->float:
    """
    Return the sum of a+b
    """
    return a+b

def sub(a:float, b:float) ->float:
    """
    Return the subtract of a-b
    """
    return a-b

def multiply(a:float, b:float)-> float:
    """
    Return the result of a*b
    """
    return a*b

def divide(a:float, b:float) -> float:
    """
    Do the division of a and b
    """
    if b != 0:
        return a/b
    else:
        print("ERROR, the denorminator can not be 0")
        return

def get_input():
    """
    Get 2 numbers and 1 operator
    """
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    oper = input("Enter the operation (+,-, *, /): ")
    return num1, num2, oper

def simple_calculator():
    """
    Do the simple+calculator in a loop until exist
    """
    print("A Simple Calculator: ")
    while True:
        num1, num2, oper = get_input()
        if oper == "+":
            print("Sum: ", add(num1, num2))
        elif oper == "-":
            print("Subtract: ", sub(num1, num2))
        elif oper == "*":
            print("Multiplication: ", multiply(num1, num2))
        elif oper == "/":
            print("Division: ", divide(num1, num2))
        else:
            print("Sorry, this operator has not been in the system yet. Please try again")
        conf = input("Do you want to continue(y/n): ")
        if conf == "n":
            print("Thank you for using the calculator!")
            return
        else:
            continue

def main():
    simple_calculator()

if __name__ == "__main__":
    main()