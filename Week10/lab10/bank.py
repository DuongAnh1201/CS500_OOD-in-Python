from customer import Customer
from customer_repository import CustomerRepository

class Bank:
    def __init__(self, bank_name: str) -> None:
        self.__bank_name = bank_name
        self.__customers: list[Customer] = []
        self.__repos = CustomerRepository()

    def load_customer(self) -> None:
        customers= self.__repos.read_customers()
        for customer in customers:
            self.__customers.append(customer)

    def add_customer(self) -> None:
        new_customer = self.__repos.add_customers()
        self.__customers.append(new_customer)
        print("Add new customer successfully!")

    def search_customer(self, account_number)->Customer|None:
        for customer in self.__customers:
            if (customer == account_number):
                print(f"Find the customer with ID {account_number}")
                return customer
        print(f"Can't find the customer with the ID {account_number}")
        return None


    def edit_customer(self, customer: Customer) -> None:
        while True:
            print("=================Edit Customer===================")
            print(customer)
            print("1. Change the account number")
            print("2. Change the customer's first name")
            print("3. Change the customer's last name")
            print("4. Change the customer's address")
            print("5. Change the customer's balance")
            print("6. Exit")
            choice = int(input("Choose the option (1-6): "))
            if choice == 1:
                new_account_number = input("New account number: ")
                if self.__repos.change_account(customer, new_account_number):
                    print("Account number updated!")
                else:
                    print(f"Account number {new_account_number} already exists!")
            elif choice == 2:
                self.__repos.change_firstname(customer, input("New first name: "))
                print("First name updated!")
            elif choice == 3:
                self.__repos.change_lastname(customer, input("New last name: "))
                print("Last name updated!")
            elif choice == 4:
                self.__repos.change_address(customer, input("New address: "))
                print("Address updated!")
            elif choice == 5:
                self.__repos.change_balance(customer, float(input("New balance: ")))
                print("Balance updated!")
            elif choice == 6:
                break

    def delete_customer(self, customer: Customer) -> None:
        self.__repos.delete_customer(customer)
        self.__customers.remove(customer)
        print("Delete customer successfully!")

    def find_negative_balance(self) -> None:
        found = False
        for customer in self.__customers:
            if customer.balance < 0:
                print(customer)
                found = True
        if not found:
            print("There is no customer with a negative balance")

    def find_max_min_balance(self) -> None:
        if not self.__customers:
            print("There is no customer")
            return
        max_customer = self.__customers[0]
        min_customer = self.__customers[0]
        for customer in self.__customers:
            if customer.balance > max_customer.balance:
                max_customer = customer
            if customer.balance < min_customer.balance:
                min_customer = customer
        print(f"Max balance: {max_customer}")
        print(f"Min balance: {min_customer}")

    def display_customer(self) -> None:
        for customer in self.__customers:
            print(customer)

def main():
    bank = Bank("SFBU Bank")
    bank.load_customer()
    bank.display_customer()

if __name__ == "__main__":
    main()