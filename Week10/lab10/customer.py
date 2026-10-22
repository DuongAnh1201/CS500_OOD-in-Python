from __future__ import annotations

class Customer:
    def __init__(self, account_number: str, firstname: str, balance: float) -> None:
        self.__account_number = account_number
        self.__firstname = firstname
        self.__balance = balance 

    def __str__(self):
        return f"Account number: {self.__account_number}\nFirst name: {self.__firstname}\nBalance: {self.__balance}"

    def to_list(self) -> list[str]:
        str = []
        str.append(self.__account_number)
        str.append(self.__firstname)
        str.append(self.__balance)

    @staticmethod
    def to_customer(row: list[str]) -> Customer:
        account_number = row[0]
        firstname = row[1]
        balance = float(row[2])
        return Customer(account_number, firstname, balance)

    @staticmethod
    def customer_information(self) -> Customer:

        try: 
