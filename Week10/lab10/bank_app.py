from bank import Bank


class BankApp:
    def __init__(self) -> None:
        self.__bank = Bank("SFBU Bank")
        self.__bank.load_customer()

    def show_menu(self) -> None:
        print("=============================================")
        print("1. Add New Customer")
        print("2. View Customer List")
        print("3. Search and Edit")
        print("4. Delete Customer")
        print("5. Find Negative Balance")
        print("6. Max/Min balance")
        print("7. Exit")

    def execute(self) -> None:
        while True:
            self.show_menu()
            choice = int(input("Enter your choice: "))
            if choice == 1:
                self.__bank.add_customer()
            elif choice == 2:
                self.__bank.display_customer()
            elif choice == 3:
                account_number = input("Type in the account number that you would search: ")
                customer = self.__bank.search_customer(account_number)
                if customer: 
                    self.__bank.edit_customer(customer)
                else:
                    print(f"There is no customer with the account number: {account_number}")
            elif choice == 4:
                account_number = input("Type in the account number that you would delete: ")
                customer = self.__bank.search_customer(account_number)
                if customer:
                    self.__bank.delete_customer(customer)
                else:
                    print(f"There is no customer with the account number: {account_number}")
            elif choice == 5:
                self.__bank.find_negative_balance()
            elif choice == 6:
                self.__bank.find_max_min_balance()
            elif choice == 7:
                break




def main():
    app =BankApp()
    app.execute()

if __name__ == "__main__":
    main()