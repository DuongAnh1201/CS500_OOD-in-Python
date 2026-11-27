from interface import GearRequestStatus
# class MaintenanceRecord:
#     def __init__(self, id: str, date: str, description: str, performed_by: str):
#         self.__id = id
#         self.__date = date
#         self.__description = description
#         self.__performed_by = performed_by
    
#     def to_row(self) -> tuple:
#         record = (self.__id, self.__date, self.__description, self.__performed_by)
#         return record

#     @staticmethod
#     def from_row(record: tuple):
#         id, date, description, performed_by = record
#         return MaintenanceRecord(id, date, description, performed_by)

class Gear:
    def __init__(self, id: str, gear_type: str, condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True)-> None:
        self.__id = id
        self.__gear_type = gear_type
        self.__condition_ratings = condition_ratings
        self.__maintenance_records = []
        for record in maintenance_records:
            self.__maintenance_records.append(record)
        self.__is_avail = is_avail  

    def update_condition(self, rating: float) -> None:
        self.__condition_ratings = rating
        print(f"Update condition rating successfully")

    def add_maintenance_record(self, record: str) -> None:
        self.__maintenance_records += f"\n" + record
        print(f"Add a new maintenance record successfully")

    def set_available(self, avail: bool) -> None:
        self.__is_avail = avail
        print(f"Set new availability successfully")

    def to_row(self) -> tuple:
        gear = (self.__id, self.__gear_type, self.__condition_ratings, self.__maintenance_records, self.__is_avail)
        return gear

class Rope(Gear):
    def __init__(self, id: str, gear_type: str = "rope", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True) -> None:
        super().__init__(id, gear_type, condition_ratings, maintenance_records, is_avail)
        
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail = row
        return Rope(id, gear_type, condition_ratings, maintenance_records, is_avail)

class Crampon(Gear):
    def __init__(self, id: str, gear_type: str = "crampon", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True) -> None:
        super().__init__(id, gear_type, condition_ratings, maintenance_records, is_avail)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail = row
        return Crampon(id,gear_type, condition_ratings, maintenance_records, is_avail)

class Beacon(Gear):
    def __init__(self, id: str, gear_type: str = "beacon", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True) -> None:
        super().__init__(id, gear_type, condition_ratings, maintenance_records, is_avail)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail = row
        return Beacon(id, gear_type, condition_ratings, maintenance_records, is_avail)

class Tent(Gear):
    def __init__(self, id: str, gear_type: str = "tent", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True) -> None:
        super().__init__(id, gear_type, condition_ratings, maintenance_records, is_avail)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail = row
        return Tent(id, gear_type, condition_ratings, maintenance_records, is_avail)

class GearRequest:
    def __init__(self, id: str, gear_type: str, quantity: int, notes: str, status: GearRequestStatus.PENDING) -> None:
        self.__id = id
        self.__gear_type = gear_type
        self.__quantity = quantity
        self.__notes = notes
        self.__status = status

    def change_status(self, status: GearRequestStatus):
        old_status = self.__status
        self.__status = status
        print(f"Successfully changed status from {old_status} to {self.__status}")

    def to_row(self) -> tuple:
        request = (self.__id, self.__gear_type, self.__quantity, self.__notes, self.__status)
        return request

    @staticmethod
    def from_row(request: tuple):
        id, gear_type, quantity, notes, status = request
        return GearRequest(id, gear_type, quantity, notes, status)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.__id}\ngear_type: {self.__gear_type}\nquantity: {self.__quantity}\nnotes: {self.__notes}\nstatus: {self.__status}"
    
class InventoryFactory:
    def __init__(self):
        self.__gear_classes: dict[str, type] = {"rope": Rope, "crampon": Crampon, "beacon": Beacon, "tent": Tent}
    
    def create_gear_by_id(self, gear_type: str, gear_id: str) -> None|Gear:
        gear = None
        if gear_type in self.__gear_classes:
            gear = self.__gear_classes[gear_type](gear_id)
        return gear

    def create_gear_by_tuple(self, gear_type: str, tuple) -> None|Gear:
        gear = None
        if gear_type in self.__gear_classes:
            gear = self.__gear_classes[gear_type].from_row(tuple)
        return gear


        