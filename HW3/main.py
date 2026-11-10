import os
from datetime import date
from customer_service import CustomerService
from vehicle_service import VehicleService
from rental_service import RentalService


class ConsoleUI:
    def __init__(self) -> None:
        self.__customer_service = CustomerService()
        self.__vehicle_service = VehicleService()
        self.__rental_service = RentalService(self.__vehicle_service, self.__customer_service)

    def show_menu(self) -> None:
        print("=============================================")
        print("1. Add New Vehicle")
        print("2. Update Vehicle")
        print("3. Add New Customer")
        print("4. Update Customer")
        print("5. Rent a Vehicle")
        print("6. Return a Vehicle")
        print("7. Search Vehicle (plate or make/model)")
        print("8. Customer List (A-Z)")
        print("9. Customer's Rentals")
        print("10. Vehicle's Rental History")
        print("11. Exit")

    def execute(self) -> None:
        while True:
            self.show_menu()
            try:
                choice = int(input("Enter your choice: "))
                if choice == 1:
                    plate = input("License plate: ")
                    make = input("Make: ")
                    model = input("Model: ")
                    year = int(input("Year: "))
                    daily_rate = float(input("Daily rate: "))
                    print(self.__vehicle_service.add_vehicle(plate, make, model, year, daily_rate))
                elif choice == 2:
                    self.__vehicle_service.update_vehicle(input("License plate of the vehicle to update: "))
                elif choice == 3:
                    firstname = input("First name: ")
                    lastname = input("Last name: ")
                    phonenumber = input("Phone number: ")
                    license = input("Driver license number: ")
                    print(self.__customer_service.add_customer(firstname, lastname, phonenumber, license))
                elif choice == 4:
                    self.__customer_service.update_customer(input("Driver license of the customer to update: "))
                elif choice == 5:
                    rental_id = int(input("Rental ID: "))
                    license = input("Customer's driver license: ")
                    plate = input("License plate: ")
                    start_date = date.fromisoformat(input("Start date (YYYY-MM-DD): "))
                    expected_return_date = date.fromisoformat(input("Expected return date (YYYY-MM-DD): "))
                    print(self.__rental_service.process_rental(rental_id, license, plate, start_date, expected_return_date))
                elif choice == 6:
                    rental_id = int(input("Rental ID: "))
                    return_date = date.fromisoformat(input("Return date (YYYY-MM-DD): "))
                    rental = self.__rental_service.process_return(rental_id, return_date)
                    print(f"Returned. Total cost: {rental.total_cost}")
                elif choice == 7:
                    plate = input("License plate (press Enter to search by make/model instead): ")
                    if plate:
                        print(self.__vehicle_service.find_by_plate(plate))
                    else:
                        make = input("Make: ")
                        model = input("Model (press Enter for every model): ")
                        for vehicle in self.__vehicle_service.search_by_make_model(make, model):
                            print(vehicle)
                elif choice == 8:
                    for customer in self.__customer_service.list_alphabetical():
                        print(customer)
                elif choice == 9:
                    license = input("Customer's driver license: ")
                    print("--- Active rentals ---")
                    for rental in self.__rental_service.get_active_rentals(license):
                        print(rental)
                    print("--- Past rentals ---")
                    for rental in self.__rental_service.get_past_rentals(license):
                        print(rental)
                elif choice == 10:
                    for rental in self.__rental_service.get_vehicle_history(input("License plate: ")):
                        print(rental)
                elif choice == 11:
                    break
            except ValueError as error: #Wrong number/date typed, or a business rule refused the action
                print(f"Error: {error}")


def main():
    os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #The repositories save to "HW3/....csv"
    app = ConsoleUI()
    app.execute()

if __name__ == "__main__":
    main()
