def calculate(adult:int, children: int, senior: int, time: str):
    ADULT_TICKET_NORMAL = 12.50
    ADULT_TICKET_WEEKEND = 15.00
    CHILDREN_TICKET_NORMAL = 8.00
    CHILDREN_TICKET_WEEKEND = 10.00
    SENIOR_TICKET_NORMAL = 9.00
    SENIOR_TICKET_WEEKEND = 11.50
    DISCOUNT = 0.10
    if time == "e" or time == "h":
        adult_ticket = ADULT_TICKET_WEEKEND*adult
        children_ticket = CHILDREN_TICKET_WEEKEND*children
        senior_ticket = SENIOR_TICKET_WEEKEND*senior
    else:
        adult_ticket = ADULT_TICKET_NORMAL*adult
        children_ticket = CHILDREN_TICKET_NORMAL*children
        senior_ticket = SENIOR_TICKET_NORMAL*senior
    OFFER = (adult+children+senior)>5
    sub_total = adult_ticket+children_ticket+senior_ticket
    if OFFER == True:
        discount = sub_total*DISCOUNT
    else: 
        discount = 0
    return adult_ticket, children_ticket, senior_ticket, sub_total, discount

def display():
    adult = int(input("Number of adult tickets: "))
    children = int(input("Number of children tickets: "))
    senior = int(input("Number of senior tickets: "))
    time = input("Is the movie showing on a weekday (w), weekend (e), holiday(h): ")
    adult_ticket, children_ticket, senior_ticket, sub_total, discount = calculate(adult, children, senior, time)
    print("Program output: \n")
    if time == "e" or time == "h":
        print(f"Adult Tickets ({adult}): $15.00 each")
        print(f"Child Tickets ({children}): $10.00 each")
        print(f"Senior Tickets ({senior}): $11.50 each")
    else:
        print(f"Adult Tickets ({adult}): $12.50 each")
        print(f"Child Tickets ({children}): $8.00 each")
        print(f"Senior Tickets ({senior}): $9.00 each")
    print(f"Subtotal: ${sub_total}")
    print(f"Discount (5+ Tickets): 10%")
    print(f"Discount amount: ${discount}")
    print(f"Total: ${sub_total-sub_total*discount}")
    print(f"Thank you for coming to the movies!")

def main():
    display()

if __name__ == "__main__":
    main()