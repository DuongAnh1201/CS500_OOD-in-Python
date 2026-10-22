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
def main():
    repos = CustomerRepository()
    customers = repos.read_customers()
    for customer in customers:
        print(customer)

if __name__ == "__main__":
    main()