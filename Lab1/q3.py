def calculate(hours:int):
    BASE_RATE = 14.50
    BASE_HOURS = 40 
    FIRST_EXCESSIVE = BASE_RATE*1.5
    SECOND_EXCESSIVE = 2.0
    TAX_RATE = 0.28
    if hours<BASE_HOURS:
        gross_pay = hours*BASE_RATE
    elif hours<=45:
        gross_pay = 40*BASE_RATE + (hours-BASE_HOURS)*FIRST_EXCESSIVE
    else:
        gross_pay = 40*BASE_RATE + 5*FIRST_EXCESSIVE + (hours-45)*SECOND_EXCESSIVE
    tax_pay = gross_pay*TAX_RATE
    net_pay = gross_pay - tax_pay
    return gross_pay, tax_pay, net_pay

def display(hours):
    gross_pay, tax_pay, net_pay = calculate(hours)
    print("Employee Pay Summary")
    print("Gross Pay: $", gross_pay)
    print("Taxes Witheld (28%): $", tax_pay)
    print("Net Pay: $", net_pay)

def main():
    while True:
        n = int(input("Enter the number of hours worked: "))
        display(n)
        i = input("Do you have another employee(yes/no): ")
        if i == 'no':
            break

if __name__ == "__main__":
    main()

        
