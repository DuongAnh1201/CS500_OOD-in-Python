"""
A program ask for inputs including: Initial investment amount
○ Annual percentage yield (APY)
○ Number of months for the CD term
○ Compounding frequency (monthly, quarterly, annually)
Then return the CD at each interval, detailed table, total interest earned
"""
def inp():
    """
    Gather basic inputs: 
    - initial investment_amount
    - annual percentage yield 
    - number of months for the CD term
    - Compounding frequency (monthly, quarterly, annually)
    """
    initial_investment_amount = float(input("Enter your initial investment amount of money: "))
    apy_in_percent = float(input("Enter annual percentage yield (APY): "))
    term = int(input("Enter number of months for the CD term: "))
    frequency = input("Enter compounding frequency (monthly, quarterly, annually): ")
    return initial_investment_amount, apy_in_percent, term, frequency

def display(month: int, cd_value: float) -> None:
    '''
    Print the monthly value
    '''
    print(f"{month:<15}{cd_value:,.2f}")
def computing():
    initial_investment_amount, apy_in_percent, term, frequency = inp()
    print(f"Month          CD Value")
    print(f"-------        -------")
    apy = apy_in_percent/100
    if frequency == "monthly":
        amount = initial_investment_amount
        #monthly percentage yield
        mpy = apy/12
        for month in range(term):
            m = month + 1
            amount = amount *(1+mpy)
            display(m, amount)
        total_interst = amount - initial_investment_amount
        print(f"Total interest earned: {total_interst:.2f}")
    elif frequency == "quarterly":
        amount = initial_investment_amount
        #quarterly percentage yield
        qpy = apy/12
        for month in range(term):
            m = month + 1
            if m%4 == 0:
                amount = amount * (1+qpy)
            display(m, amount)
        total_interst = amount - initial_investment_amount
        print(f"Total interest earned: {total_interst:.2f}")
    elif frequency == "annually":
        amount = initial_investment_amount
        for month in range(term):
            m = month + 1
            if m%12 == 0:
                amount = amount * (1+apy)
            display(m, amount)
        total_interst = amount - initial_investment_amount
        print(f"Total interest earned: {total_interst:.2f}")

    
def main():
    computing()

if __name__ == "__main__":
    main()

