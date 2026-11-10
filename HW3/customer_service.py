from customer import Customer
from customer_repository import CustomerRepository

class CustomerService:
    def __init__(self) -> None:
        self.__repository = CustomerRepository() #The presentation layer never touches the data layer

    def add_customer(self, firstname: str, lastname: str, phonenumber: str, driver_license_number: str) -> Customer:
        '''
        Make sure the license is not used yet, then save the new customer
        '''
        firstname, lastname = firstname.strip(), lastname.strip()
        phonenumber, driver_license_number = phonenumber.strip(), driver_license_number.strip()
        if self.__repository.find_by_license(driver_license_number) is not None:
            raise ValueError(f"A customer with driver license {driver_license_number} already exists.")
        new_customer = Customer(firstname, lastname, phonenumber, driver_license_number)
        customers = self.__repository.read_customers() 
        customers.append(new_customer) 
        self.__repository.save_customers(customers)
        return new_customer

    UPDATE_OPTIONS = ["Change first name", "Change last name", "Change phone number", "Change driver license number"] #Option 1 to 4, 0 is Done

    def update_customer(self, license: str) -> Customer:
        '''
        Keep showing the update menu until the user chooses 0. Done
        '''
        customer = self.find_by_license(license)
        while True:
            print(f"\nUpdating: {customer}")
            for number, text in enumerate(self.UPDATE_OPTIONS, 1):
                print(f"{number}. {text}")
            print("0. Done")
            option = input("Choose an option: ").strip()
            if option == "0":
                break
            if option not in ("1", "2", "3", "4"):
                print(f"Option must be a number from 0 to {len(self.UPDATE_OPTIONS)}.")
                continue
            new_value = input("Enter the new value: ").strip()
            if option == "1":
                self.__repository.change_firstname(customer, new_value)
            elif option == "2":
                self.__repository.change_lastname(customer, new_value)
            elif option == "3":
                self.__repository.change_phonenumber(customer, new_value)
            elif option == "4":
                if new_value != customer.driver_license_number and self.__repository.find_by_license(new_value) is not None:
                    print(f"A customer with driver license {new_value} already exists.")
                    continue
                self.__repository.change_license(customer, new_value)
            print("Updated.")
        return customer

    def find_by_license(self, driver_license_number: str) -> Customer:
        customer = self.__repository.find_by_license(driver_license_number.strip())
        if customer is None:
            raise ValueError(f"No customer with driver license {driver_license_number}.")
        return customer

    def list_alphabetical(self) -> list[Customer]:
        '''
        All customers sorted by last name, then first name (upper/lower case does not matter)
        '''
        return sorted(self.__repository.read_customers(), key=lambda customer: (customer.lastname.lower(), customer.firstname.lower()))


if __name__=="__main__":
    pass
