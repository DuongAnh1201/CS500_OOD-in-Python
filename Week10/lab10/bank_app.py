from calendar import c
from bank import Bank
from customer import Customer


class BankApp:
    def __init__(self) -> None:
        self.__bank = Bank("SFBU Bank")
        self.__bank.load_customer()

    def show_menu(self) -> None:
        print("=============================================")
        print("1. Show All Customers")
        print("2. Add New Customer")
        print("10. Exit")

    def execute(self) -> None:
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.__bank.display_customer()
            elif choice == 10:
                break

def test():
    pass

def main():
    app =BankApp()
    app.execute()

if __name__ == "__main__":
    main()