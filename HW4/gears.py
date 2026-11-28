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
    def __init__(self, gear_type: str, condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True, booked_dates: list[str] = [], gear_id: str = "")-> None:
        self.__id = "gear" + str(id(self))
        self.__gear_type = gear_type
        self.__condition_ratings = condition_ratings
        # records are kept as one text, one record per line
        self.__maintenance_records = maintenance_records
        self.__is_avail = is_avail
        # days this gear is already booked, full-day allocation, e.g. ["2026-12-01", "2026-12-02"]
        self.__booked_dates = []
        for date in booked_dates:
            self.__booked_dates.append(date)
        if gear_id!= "":
            self.__id = gear_id

    def update_condition(self, rating: float) -> None:
        self.__condition_ratings = rating
        print(f"Update condition rating successfully")

    def add_maintenance_record(self, record: str) -> None:
        if self.__maintenance_records == "":
            self.__maintenance_records = record
        else:
            self.__maintenance_records += f"\n" + record
        print(f"Add a new maintenance record successfully")

    def set_available(self, avail: bool) -> None:
        self.__is_avail = avail
        print(f"Set new availability successfully")

    def is_free(self, dates: list[str]) -> bool:
        '''True if the gear is in service and not booked on any of these days'''
        if not self.__is_avail:
            return False
        for date in dates:
            if date in self.__booked_dates:
                return False
        return True

    def book(self, dates: list[str]) -> None:
        for date in dates:
            if date not in self.__booked_dates:
                self.__booked_dates.append(date)
        print(f"Book gear for {dates} successfully")

    def release(self, dates: list[str]) -> None:
        for date in dates:
            if date in self.__booked_dates:
                self.__booked_dates.remove(date)
        print(f"Release gear for {dates} successfully")

    def to_row(self) -> tuple:
        gear = (self.__id, self.__gear_type, self.__condition_ratings, self.__maintenance_records, self.__is_avail, self.__booked_dates)
        return gear

class Rope(Gear):
    def __init__(self, gear_type: str = "rope", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True, booked_dates: list[str] = [], gear_id: str = "") -> None:
        super().__init__(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, gear_id)
        
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail, booked_dates = row
        return Rope(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, id)

class Crampon(Gear):
    def __init__(self, gear_type: str = "crampon", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True, booked_dates: list[str] = [], gear_id: str = "") -> None:
        super().__init__(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, gear_id)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail, booked_dates = row
        return Crampon(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, id)

class Beacon(Gear):
    def __init__(self, gear_type: str = "beacon", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True, booked_dates: list[str] = [], gear_id: str = "") -> None:
        super().__init__(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, gear_id)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail, booked_dates = row
        return Beacon(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, id)

class Tent(Gear):
    def __init__(self, gear_type: str = "tent", condition_ratings: float = 5, maintenance_records: str = "", is_avail: bool = True, booked_dates: list[str] = [], gear_id: str = "") -> None:
        super().__init__(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, gear_id)
    @staticmethod
    def from_row(row: tuple):
        id, gear_type, condition_ratings, maintenance_records, is_avail, booked_dates = row
        return Tent(gear_type, condition_ratings, maintenance_records, is_avail, booked_dates, id)

class GearRequest:
    def __init__(self, gear_type: str, quantity: int, notes: str, status: GearRequestStatus.PENDING, gear_request_id: str = "") -> None:
        self.__id = "gear_request" + str(id(self))
        self.__gear_type = gear_type
        self.__quantity = quantity
        self.__notes = notes
        self.__status = status
        if gear_request_id != "":
            self.__id = gear_request_id

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
        return GearRequest(gear_type, quantity, notes, status, id)

    @property
    def id(self):
        return self.__id

    def __str__(self):
        return f"ID: {self.__id}\ngear_type: {self.__gear_type}\nquantity: {self.__quantity}\nnotes: {self.__notes}\nstatus: {self.__status}"
    
class InventoryFactory:
    def __init__(self):
        self.__gear_classes: dict[str, type] = {"rope": Rope, "crampon": Crampon, "beacon": Beacon, "tent": Tent}
    
    def create_gear_by_id(self, gear_type: str, gear_id: str = "") -> None|Gear:
        '''leave gear_id empty for a new gear, so Gear makes a unique ID'''
        gear = None
        if gear_type in self.__gear_classes:
            gear = self.__gear_classes[gear_type](gear_id=gear_id)
        return gear

    def create_gear_by_tuple(self, gear_type: str, tuple) -> None|Gear:
        gear = None
        if gear_type in self.__gear_classes:
            gear = self.__gear_classes[gear_type].from_row(tuple)
        return gear


        