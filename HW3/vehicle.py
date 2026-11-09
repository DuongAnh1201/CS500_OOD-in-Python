class Vehicle:
    def __init__(self, license_plate_number: str, make: str, model: str, year: int, daily_rate: float, available: bool) -> None:
        self.__license_plate_number = license_plate_number
        self.__make = make
        self.__model = model
        self.__year = year
        self.__daily_rate = daily_rate
        self.__available = available

    @property
    def license_plate_number(self) -> str:
        return self.__license_plate_number
    
    def to_list(self) -> list[str]:
        return [self.__license_plate_number, self.__make, self.__model, str(self.__year), str(self.__daily_rate), str(self.__available)]

    @staticmethod
    def to_vehicle(row: list[str]) -> 'Vehicle':
        return Vehicle(row[0], row[1], row[2], int(row[3]), float(row[4]), bool(row[5]))
    
    @staticmethod
    def vehicle_information() -> 'Vehicle':
        return Vehicle.to_vehicle(input("Enter the vehicle information: ").split(","))
    
    def __str__(self) -> str:
        return f"License Plate Number: {self.__license_plate_number}, Make: {self.__make}, Model: {self.__model}, Year: {self.__year}, Daily Rate: {self.__daily_rate}, Available: {self.__available}"
    
    def __eq__(self, other) -> bool:
        if isinstance(other, Vehicle):
            return self.__license_plate_number == other.__license_plate_number
        return False

    @property
    def daily_rate(self) -> float:
        return self.__daily_rate
    
    @property
    def available(self) -> bool:
        return self.__available
    
    @available.setter
    def available(self, available: bool) -> None:
        self.__available = available