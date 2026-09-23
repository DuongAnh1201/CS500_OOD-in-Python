from enum import Enum

class Applicant:
    def __init__(self, full_name: str, contact_number: str, email_address: str, address: str):
        self.__full_name = full_name
        self.__contact_number = contact_number
        self.__email_address = email_address
        self.__address = address
    @property
    def full_name(self) -> str:
        return self.__full_name
    full_name.setter
    def full_name(self, new_full_name: str) -> None:
        self.__full_name = new_full_name
    @property
    def contact_number(self) -> str:
        return self.__contact_number
    @contact_number.setter
    def contact_number(self, new_contact_number: str) -> None:
        self.__contact_number = new_contact_number
    @property
    def email_address(self) -> str:
        return self.__email_address
    @email_address.setter
    def email_address(self, new_email_address: str) -> None:
        self.__email_address = new_email_address
    @property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, new_address: str) -> None:
        self.__address = new_address
    

    def __str__(self):
        return f"Full name: {self.__full_name}\nContact number: {self.__contact_number}\nEmail address: {self.__email_address}\nAddress: {self.__address}"

class ApplicationStatus(Enum):
    PENDING = 0
    REVIEWED = 1 
    REJECTED = 2
    ACCEPTED = 3

