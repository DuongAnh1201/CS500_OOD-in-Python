import csv
import os
from vehicle import Vehicle

class VehicleRepository:
    def __init__(self):
        self.__filepath = "HW3/vehicle.csv"
        if not os.path.exists(self.__filepath): #Create an empty file on the first run
            open(self.__filepath, "w").close()

    def read_vehicles(self) -> list[Vehicle]:
        vehicles = []
        with open(self.__filepath, "r", newline="") as file:
            reader = csv.reader(file, delimiter = ";")
            for row in reader:
                vehicles.append(Vehicle.to_vehicle(row))
        return vehicles

    def save_vehicles(self, vehicles: list[Vehicle]) -> None:
        with open(self.__filepath, "w", newline="") as file:
            writer = csv.writer(file, delimiter= ";")
            for vehicle in vehicles:
                writer.writerow(vehicle.to_list())

    def add_vehicle(self, vehicle: Vehicle) -> None:
        '''
        Both add to the list and save to the data
        '''
        vehicles = self.read_vehicles() #Read to the file first
        vehicles.append(vehicle) #Saved to the list first.
        self.save_vehicles(vehicles)

    def __update_vehicle(self, old_plate: str, vehicle: Vehicle) -> None:
        '''
        Replace the row with old_plate by the edited vehicle and save the file
        '''
        vehicles = self.read_vehicles()
        for index, row_vehicle in enumerate(vehicles):
            if row_vehicle.license_plate_number == old_plate:
                vehicles[index] = vehicle
                break
        self.save_vehicles(vehicles)

    def change_plate(self, vehicle: Vehicle, new_plate: str) -> bool:
        '''
        Return False (and change nothing) when another vehicle already uses new_plate
        '''
        if self.find_by_plate(new_plate) is not None:
            return False
        old_plate = vehicle.license_plate_number
        vehicle.license_plate_number = new_plate
        self.__update_vehicle(old_plate, vehicle)
        return True

    def change_make(self, vehicle: Vehicle, new_make: str):
        vehicle.make = new_make
        self.__update_vehicle(vehicle.license_plate_number, vehicle)

    def change_model(self, vehicle: Vehicle, new_model: str):
        vehicle.model = new_model
        self.__update_vehicle(vehicle.license_plate_number, vehicle)

    def change_year(self, vehicle: Vehicle, new_year: int):
        vehicle.year = new_year
        self.__update_vehicle(vehicle.license_plate_number, vehicle)

    def change_daily_rate(self, vehicle: Vehicle, new_rate: float):
        vehicle.daily_rate = new_rate
        self.__update_vehicle(vehicle.license_plate_number, vehicle)

    def change_availability(self, vehicle: Vehicle, available: bool):
        vehicle.available = available
        self.__update_vehicle(vehicle.license_plate_number, vehicle)

    def delete_vehicle(self, vehicle: Vehicle) -> None:
        vehicles = self.read_vehicles()
        vehicles.remove(vehicle)
        self.save_vehicles(vehicles)

    def find_by_plate(self, plate: str) -> Vehicle:
        '''
        Return the vehicle with this license plate number, or None if there is no one
        '''
        for vehicle in self.read_vehicles():
            if vehicle.license_plate_number == plate:
                return vehicle
        return None

if __name__=="__main__":
    pass
