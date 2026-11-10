import csv
import os
from datetime import date
from rental import Rental
from customer_repository import CustomerRepository
from vehicle_repository import VehicleRepository

class RentalRepository:

    def __init__(self, customer_repo: CustomerRepository, vehicle_repo: VehicleRepository) -> None:
        self.__filename = "HW3/rentals.csv"
        self.__customer_repo = customer_repo #Used to turn a license back into a Customer
        self.__vehicle_repo = vehicle_repo #Used to turn a plate back into a Vehicle
        if not os.path.exists(self.__filename): #Create an empty file on the first run
            open(self.__filename, "w").close()

    def read_rentals(self) -> list[Rental]:
        '''
        Each row only keeps the license and the plate,
        so the Customer and Vehicle objects are looked up from the other repositories
        '''
        rentals = []
        with open(self.__filename, "r", newline="") as file:
            reader = csv.reader(file, delimiter = ";")
            for row in reader:
                customer = self.__customer_repo.find_by_license(row[1])
                vehicle = self.__vehicle_repo.find_by_plate(row[2])
                if customer is None or vehicle is None: #The customer or vehicle was deleted
                    continue
                rentals.append(Rental.to_rental(row, customer, vehicle))
        return rentals

    def save_rentals(self, rentals: list[Rental]) -> None:
        with open(self.__filename, "w", newline="") as file:
            writer = csv.writer(file, delimiter= ";")
            for rental in rentals:
                writer.writerow(rental.to_list())

    def add_rental(self, rental: Rental) -> None:
        '''
        Save the new rental and mark its vehicle as not available
        '''
        rentals = self.read_rentals() #Read to the file first
        rentals.append(rental) #Saved to the list first.
        self.save_rentals(rentals)
        self.__vehicle_repo.change_availability(rental.vehicle, False)

    def __update_rental(self, rental: Rental) -> None:
        '''
        Replace the row with the same rental id by the edited rental and save the file
        '''
        rentals = self.read_rentals()
        for index, row_rental in enumerate(rentals):
            if row_rental.rental_id == rental.rental_id:
                rentals[index] = rental
                break
        self.save_rentals(rentals)

    def return_rental(self, rental: Rental, return_date: date) -> None:
        '''
        Close the rental and make its vehicle available again
        '''
        rental.actual_return_date = return_date
        self.__update_rental(rental)
        self.__vehicle_repo.change_availability(rental.vehicle, True)

    def delete_rental(self, rental: Rental) -> None:
        rentals = self.read_rentals()
        rentals.remove(rental)
        self.save_rentals(rentals)

if __name__=="__main__":
    pass
