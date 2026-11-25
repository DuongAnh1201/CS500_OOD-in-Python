class MaintenanceRecord:
    def __init__(self, id: str, date: str, description: str, performed_by: str):
        self.__id = id
        self.__date = date
        self.__description = description
        self.__performed_by = performed_by
    
    def to_row(self) -> tuple:
        record = (self.__id, self.__date, self.__description, self.__performed_by)
        return record

    @staticmethod
    def from_row(record: tuple):
        id, date, description, performed_by = record
        return MaintenanceRecord(id, date, description, performed_by)

class Gear:
    def __init__(self, id: str, condition_ratings: float, maintenance_records: list[MaintenanceRecord], is_avail: bool)-> None:
        self.__id = id
        self.__condition_ratings = condition_ratings
        self.__maintenance_records = []
        for record in maintenance_records:
            self.__maintenance_records.append(record)
        self.__is_avail = is_avail  

    def update_condition(self, rating: float) -> None:
        self.__condition_ratings = rating
        print(f"Update condition rating successfully")

    def add_maintenance_record(self, record: MaintenanceRecord) -> None:
        self.__maintenance_records.append(record)
        print(f"Add a new maintenance record successfully")

    def set_available(self, avail: bool) -> None:
        self.__is_avail = avail
        print(f"Set new availability successfully")

    def to_row(self) -> tuple:
        gear = (self.__id, self.__condition_ratings, self.__maintenance_records, self.__is_avail)
        return gear

class Rope(Gear):
    def __init__(self, id: str, condition_ratings: float, maintenance_records: list[MaintenanceRecord], is_avail: bool) -> None:
        super().__init__()
    @staticmethod
    def from_row(row: tuple):
        id, condition_ratings, maintenance_records, is_avail = tuple
        return Rope(id, condition_ratings, maintenance_records, is_avail)

class Crampon(Gear):
    def __init__(self, id: str, condition_ratings: float, maintenance_records: list[MaintenanceRecord], is_avail: bool) -> None:
        super().__init__()
    @staticmethod
    def from_row(row: tuple):
        id, condition_ratings, maintenance_records, is_avail = tuple
        return Crampon(id, condition_ratings, maintenance_records, is_avail)

class Beacon(Gear):
    def __init__(self, id: str, condition_ratings: float, maintenance_records: list[MaintenanceRecord], is_avail: bool) -> None:
        super().__init__()
    @staticmethod
    def from_row(row: tuple):
        id, condition_ratings, maintenance_records, is_avail = tuple
        return Beacon(id, condition_ratings, maintenance_records, is_avail)

class Tent(Gear):
    def __init__(self, id: str, condition_ratings: float, maintenance_records: list[MaintenanceRecord], is_avail: bool) -> None:
        super().__init__()
    @staticmethod
    def from_row(row: tuple):
        id, condition_ratings, maintenance_records, is_avail = tuple
        return Tent(id, condition_ratings, maintenance_records, is_avail)