class Person:
    def __init__(self, firstname: str, lastname: str, phonenumber: str) -> None:
        self.__firstname = firstname
        self.__lastname = lastname
        self.__phonenumber = phonenumber

    @property
    def firstname(self) -> str:
        return self.__firstname
    @firstname.setter
    def firstname(self, new_firstname) -> None:
        self.__firstname = new_firstname

    @property
    def lastname(self) -> str:
        return self.__lastname
    @lastname.setter
    def lastname(self, new_lastname) -> None:
        self.__lastname = new_lastname

    @property
    def phonenumber(self) -> str:
        return self.__phonenumber
    @phonenumber.setter
    def phonenumber(self, new_phone) -> None:
        self.__phonenumber = new_phone

    def __str__(self) -> str:
        return f"First Name: {self.__firstname}, Last Name: {self.__lastname}, Phone Number: {self.__phonenumber}"
    

class Customer(Person):
    def __init__(self, firstname: str, lastname: str, phonenumber: str, driver_license_number: str) -> None:
        super().__init__(firstname, lastname, phonenumber)
        self.__driver_license_number = driver_license_number

    @property
    def driver_license_number(self) -> str:
        return self.__driver_license_number
    @driver_license_number.setter
    def driver_license_number(self, new_license) -> None:
        self.__driver_license_number = new_license
        

    def __str__(self) -> str:
        return super().__str__() + f", Driver License Number: {self.__driver_license_number}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Customer):
            return self.__driver_license_number == other.__driver_license_number
        return False
        
    def to_list(self) -> list[str]: #Used to write to the customer.txt file
        return [self.firstname, self.lastname, self.phonenumber, self.__driver_license_number]
        
    @staticmethod
    def to_customer(row: list[str]) -> 'Customer': #Used to read from the customer.txt file
        firstname = row[0]
        lastname = row[1]
        phonenumber = row[2]
        driver_license_number = row[3]
        return Customer(firstname, lastname, phonenumber, driver_license_number)

    @staticmethod
    def customer_information() -> 'Customer':
        firstname: str = input("Enter your first name: ")
        lastname: str = input("Enter your last name: ")
        phonenumber: str = input("Enter your phone number: ")
        driver_license_number: str = input("Enter your driver license number: ")
        return Customer(firstname, lastname, phonenumber, driver_license_number)
        
        
        
