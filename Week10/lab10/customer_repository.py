import csv
from customer import Customer

class CustomerRepository:
    def __init__(self) -> None:
        self.__filename = "lab10/customers.csv"

    
    def read_customers(self) -> list[Customer]:
        customers = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file,delimiter=";")
            for row in reader:
                customers.append(Customer.to_customer(row))
        return customers

    def save_customers(self, customers: list[Customer]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter=";")
            for customer in customers:
                writer.writerow(customer.to_list())

    def add_customers(self): 
        '''
        Both add to the list and save to the data.
        '''
        #Read to the file first
        new_customer: Customer = Customer.customer_information()
        customers = self.read_customers()
        customers.append(new_customer)
        self.save_customers(customers)
        return new_customer

    def __update_customer(self, old_account_number: str, customer: Customer) -> None:
        '''
        Replace the row with old_account_number by the edited customer and save the file.
        '''
        customers = self.read_customers()
        for index, row_customer in enumerate(customers):
            if row_customer == old_account_number:
                customers[index] = customer
                break
        self.save_customers(customers)

    def change_account(self, customer: Customer, new_account_number: str) -> bool:
        '''
        update the customer information in the database layer
        '''
        # account number is the key, so it must stay unique
        if new_account_number in self.read_customers():
            return False
        old_account_number = customer.account_number
        customer.account_number = new_account_number
        self.__update_customer(old_account_number, customer)
        return True

    def change_firstname(self, customer: Customer, new_firstname: str) -> None:
        customer.firstname = new_firstname
        self.__update_customer(customer.account_number, customer)

    def change_lastname(self, customer: Customer, new_lastname: str) -> None:
        customer.lastname = new_lastname
        self.__update_customer(customer.account_number, customer)

    def change_address(self, customer: Customer, new_address: str) -> None:
        customer.address = new_address
        self.__update_customer(customer.account_number, customer)

    def change_balance(self, customer: Customer, new_balance: float) -> None:
        customer.balance = new_balance
        self.__update_customer(customer.account_number, customer)

    def delete_customer(self, customer: Customer) -> None:
        customers = self.read_customers()
        customers.remove(customer)
        self.save_customers(customers)

def main():
    repos = CustomerRepository()
    customers = repos.read_customers()
    for customer in customers:
        print(customer)

if __name__ == "__main__":
    main()