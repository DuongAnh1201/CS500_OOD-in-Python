from customer import Customer
from vehicle import Vehicle
from datetime import date
from typing import Optional
class Rental:
    RENTAL_ID = 1000
    def __init__(self, rental_id: int, customer: Customer, vehicle: Vehicle, start_date: date, expected_return_date: date, actual_return_date: date, total_cost: float) -> None:
        self.__rental_id = rental_id
        self.__customer = customer
        self.__vehicle = vehicle
        self.__start_date = start_date
        self.__expected_return_date = expected_return_date
        self.__actual_return_date = actual_return_date
        self.__total_cost = total_cost

    def __str__(self) -> str:
        return f"Rental ID: {self.__rental_id}, Customer: {self.__customer}, Vehicle: {self.__vehicle}, Start Date: {self.__start_date}, Expected Return Date: {self.__expected_return_date}, Actual Return Date: {self.__actual_return_date}, Total Cost: {self.__total_cost}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Rental):
            return self.__rental_id == other.__rental_id and self.__customer == other.__customer and self.__vehicle == other.__vehicle and self.__start_date == other.__start_date and self.__expected_return_date == other.__expected_return_date and self.__actual_return_date == other.__actual_return_date and self.__total_cost == other.__total_cost
        return False

    @property
    def rental_id(self) -> int:
        return self.__rental_id
    
    @property
    def customer(self) -> Customer:
        return self.__customer
    
    @property
    def vehicle(self) -> Vehicle:
        return self.__vehicle
    
    @property
    def start_date(self) -> date:
        return self.__start_date
    
    @property
    def expected_return_date(self) -> date:
        return self.__expected_return_date
    
    @property
    def actual_return_date(self) -> date:
        return self.__actual_return_date
    @actual_return_date.setter
    def actual_return_date(self, return_date: date) -> None:
        self.__actual_return_date = return_date
    
    @property
    def total_cost(self) -> float:
        return self.__total_cost

    def is_active(self) -> bool:
        return self.__actual_return_date is None

    def to_list(self) -> list[Optional[str]]:
        actual_return = self.__actual_return_date.strftime("%Y-%m-%d") if self.__actual_return_date else ""
        return [str(self.__rental_id), self.__customer.driver_license_number, self.__vehicle.license_plate_number, self.__start_date.strftime("%Y-%m-%d"), self.__expected_return_date.strftime("%Y-%m-%d"), actual_return, str(self.__total_cost)]

    @staticmethod
    def to_rental(row: list[Optional[str]], customer: Customer, vehicle: Vehicle) -> 'Rental':
        actual_return_date = date.fromisoformat(row[5]) if row[5] else None
        return Rental(int(row[0]), customer, vehicle, date.fromisoformat(row[3]), date.fromisoformat(row[4]), actual_return_date, float(row[6]))
        
    @staticmethod
    def rental_information() -> 'Rental':
        return Rental.to_rental(input("Enter the rental information: ").split(","))