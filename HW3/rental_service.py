from datetime import date
from rental import Rental
from rental_repository import RentalRepository
from customer_service import CustomerService
from vehicle_service import VehicleService

class RentalService:
    def __init__(self, repository: RentalRepository, vehicle_service: VehicleService, customer_service: CustomerService) -> None:
        self.__repository = repository
        self.__vehicle_service = vehicle_service
        self.__customer_service = customer_service

    def process_rental(self, rental_id: int, driver_license_number: str, license_plate_number: str, start_date: date, expected_return_date: date) -> Rental:
        for rental in self.__repository.read_rentals():
            if rental.rental_id == rental_id:
                raise ValueError(f"A rental with ID {rental_id} already exists.")
        customer = self.__customer_service.find_by_license(driver_license_number)
        vehicle = self.__vehicle_service.find_by_plate(license_plate_number)
        if not vehicle.available:
            raise ValueError(f"Vehicle {vehicle.license_plate_number} is already rented.")
        if expected_return_date <= start_date:
            raise ValueError("The expected return date must be after the start date.")
        total_cost = self.__calculate_cost(vehicle.daily_rate, start_date, expected_return_date)
        new_rental = Rental(rental_id, customer, vehicle, start_date, expected_return_date, None, total_cost)
        self.__repository.add_rental(new_rental) #Also marks the vehicle as not available
        return new_rental

    def process_return(self, rental_id: int, return_date: date) -> Rental:
        '''
        Close the rental and make the vehicle available again.
        '''
        rental = self.__find_rental(rental_id)
        if not rental.is_active():
            raise ValueError(f"Rental {rental_id} was already returned on {rental.actual_return_date}.")
        if return_date < rental.start_date:
            raise ValueError("The return date cannot be before the start date.")
        if return_date > rental.expected_return_date:
            rental.total_cost = self.__calculate_cost(rental.vehicle.daily_rate, rental.start_date, return_date)
        self.__repository.return_rental(rental, return_date) 
        return rental

    def get_customer_rentals(self, driver_license_number: str) -> list[Rental]:
        customer = self.__customer_service.find_by_license(driver_license_number)
        rentals = []
        for rental in self.__repository.read_rentals():
            if rental.customer == customer:
                rentals.append(rental)
        return rentals

    def get_active_rentals(self, driver_license_number: str) -> list[Rental]:
        rentals = []
        for rental in self.get_customer_rentals(driver_license_number):
            if rental.is_active():
                rentals.append(rental)
        return rentals

    def get_past_rentals(self, driver_license_number: str) -> list[Rental]:
        rentals = []
        for rental in self.get_customer_rentals(driver_license_number):
            if not rental.is_active():
                rentals.append(rental)
        return rentals

    def get_vehicle_history(self, license_plate_number: str) -> list[Rental]:
        vehicle = self.__vehicle_service.find_by_plate(license_plate_number)
        rentals = []
        for rental in self.__repository.read_rentals():
            if rental.vehicle == vehicle:
                rentals.append(rental)
        return rentals

    def __find_rental(self, rental_id: int) -> Rental:
        for rental in self.__repository.read_rentals():
            if rental.rental_id == rental_id:
                return rental
        raise ValueError(f"No rental with ID {rental_id}.")

    def __calculate_cost(self, daily_rate: float, start_date: date, end_date: date) -> float:
        days = max((end_date - start_date).days, 1)
        return round(days * daily_rate, 2)

if __name__=="__main__":
    pass
