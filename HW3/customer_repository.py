import csv
from tkinter import N
from customer import Customer

class CustomerRepository:
    def __init__(self) -> None:
        self.__filename = "HW3/customers.csv"

    def read_customers(self) -> list[Customer]:
        customers = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file, delimiter = ";")
            for row in reader:
                customers.append(Customer.to_customer(row))
        return customers

    def save_customers(self, customers: list[Customer]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter= ";")
            for customer in customers:
                writer.writerow(customer.to_list())

    def add_customer(self) -> Customer:
        '''
        Both add to the list and save to the data
        '''
        #Read to the file first

        new_customer: Customer = Customer.customer_information()
        customers = self.read_customers()
        customers.append(new_customer) #Saved to the list first.
        self.save_customers(customers)
        return customers #return the new list, so in the console, no need to rewrite

    def __update_customer(self, old_license: str, customer: Customer) -> None:
        '''
        Replace the row with old_account_number by the edited customer and save the file
        '''
        customers = self.read_customers()
        for index, row_customer in enumerate(customers):
            if row_customer == old_license:
                customers[index] = customer
                break
        self.save_customers(customers)

    def change_license(self, customer: Customer, new_license: str):
        old_license = customer.driver_license_number
        customer.driver_license_number = new_license
        self.__update_customer(old_license, customer)

    def change_firstname(self, customer: Customer, new_firstname: str):
        customer.firstname = new_firstname
        self.__update_customer(customer.driver_license_number, customer)

    def change_lastname(self, customer: Customer, new_lastname: str):
        customer.lastname = new_lastname
        self.__update_customer(customer.driver_license_number, customer)

    def change_phonenumber(self, customer: Customer, new_phone: str):
        customer.phonenumber = new_phone
        self.__update_customer(customer.driver_license_number, customer)

    def delete_customer(self, customer: Customer) -> None:
        customers = self.read_customers()
        customers.remove(customer)
        self.save_customers(customers)

if __name__=="__main__":
    pass