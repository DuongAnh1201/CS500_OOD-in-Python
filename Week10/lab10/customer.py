from __future__ import annotations

class Customer:
    def __init__(self, account_number: str, firstname: str, lastname: str, address: str, balance: float) -> None:
        self.__account_number = account_number
        self.__firstname = firstname
        self.__lastname = lastname
        self.__address = address
        self.__balance = balance 
        

    def __str__(self):
        return f"Account number: {self.__account_number}; First name: {self.__firstname}; Last Name: {self.__lastname}; Address: {self.__address}; Balance: {self.__balance};"

    @property
    def account_number(self) -> str:
        return self.__account_number

    @account_number.setter
    def account_number(self, value: str) -> None:
        self.__account_number = value

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, value: str) -> None:
        self.__firstname = value

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, value: str) -> None:
        self.__lastname = value

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @property
    def balance(self) -> float:
        return self.__balance

    @balance.setter
    def balance(self, value: float) -> None:
        self.__balance = value

    def to_list(self) -> list[str]:
        str = []
        str.append(self.__account_number)
        str.append(self.__firstname)
        str.append(self.__lastname)
        str.append(self.__address)
        str.append(self.__balance)
        return str

    def __eq__(self, target) -> bool:
        if isinstance(target, Customer):
            return target.__account_number == self.__account_number
        if isinstance(target, str):
            return target == self.__account_number
        return False

    @staticmethod
    def to_customer(row: list[str]) -> Customer:
        account_number = row[0]
        firstname = row[1]
        lastname = row[2]
        address = row[3]
        balance = float(row[4])
        return Customer(account_number, firstname, lastname, address, balance)

    @staticmethod
    def customer_information() -> Customer:
        account_number: str = input("Type in new customer's account number: ")
        firstname: str = input("New customer's first name: ")
        lastname: str = input("New customer's last name: ")
        address: str = input("New customer's address: ")
        balance: float = float(input("New customer's balance: "))
        return Customer(account_number, firstname, lastname, address, balance)
        
        
