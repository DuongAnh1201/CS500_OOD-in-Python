from vehicle import Vehicle
from vehicle_repository import VehicleRepository

class VehicleService:
    def __init__(self, repository: VehicleRepository) -> None:
        self.__repository = repository

    def add_vehicle(self, vehicle: Vehicle) -> Vehicle:
        if self.__repository.find_by_plate(vehicle.license_plate_number) is not None:
            raise ValueError(f"A vehicle with plate {vehicle.license_plate_number} already exists.")
        vehicle.available = True #A new vehicle is always ready to rent
        self.__repository.add_vehicle(vehicle)
        return vehicle

    UPDATE_OPTIONS = ["Change license plate", "Change make", "Change model", "Change year", "Change daily rate"] #Option 1 to 5, 0 is Done

    def update_vehicle(self, plate: str) -> Vehicle:
        vehicle = self.find_by_plate(plate)
        while True:
            print(f"\nUpdating: {vehicle}")
            for number, text in enumerate(self.UPDATE_OPTIONS, 1):
                print(f"{number}. {text}")
            print("0. Done")
            option = input("Choose an option: ").strip()
            if option == "0":
                break
            if option not in ("1", "2", "3", "4", "5"):
                print(f"Option must be a number from 0 to {len(self.UPDATE_OPTIONS)}.")
                continue
            new_value = input("Enter the new value: ").strip()
            if option == "1":
                if not vehicle.available:
                    print("The plate of a rented vehicle cannot be changed.")
                    continue
                if new_value != vehicle.license_plate_number and self.__repository.find_by_plate(new_value) is not None:
                    print(f"A vehicle with plate {new_value} already exists.")
                    continue
                self.__repository.change_plate(vehicle, new_value)
            elif option == "2":
                self.__repository.change_make(vehicle, new_value)
            elif option == "3":
                self.__repository.change_model(vehicle, new_value)
            elif option == "4":
                try:
                    self.__repository.change_year(vehicle, int(new_value))
                except ValueError:
                    print("Year must be a whole number.")
                    continue
            elif option == "5":
                try:
                    self.__repository.change_daily_rate(vehicle, float(new_value))
                except ValueError:
                    print("Daily rate must be a number.")
                    continue
            print("Updated.")
        return vehicle

    def find_by_plate(self, license_plate_number: str) -> Vehicle:
        vehicle = self.__repository.find_by_plate(license_plate_number.strip())
        if vehicle is None:
            raise ValueError(f"No vehicle with plate {license_plate_number}.")
        return vehicle

    def search_by_make_model(self, make: str, model: str = "") -> list[Vehicle]:
        '''
        Upper/lower case does not matter. Leave model empty to get every model of that make
        '''
        make, model = make.strip().lower(), model.strip().lower()
        vehicles = []
        for vehicle in self.__repository.read_vehicles():
            if vehicle.make.lower() == make and (model == "" or vehicle.model.lower() == model):
                vehicles.append(vehicle)
        return vehicles

    def list_available(self) -> list[Vehicle]:
        vehicles = []
        for vehicle in self.__repository.read_vehicles():
            if vehicle.available:
                vehicles.append(vehicle)
        return vehicles

if __name__=="__main__":
    pass
