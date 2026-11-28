from expedition import ExpeditionWindow
from person import Customer
from gears import Gear, GearRequest
from interface import ReservationStatus
class Reservation:
    def __init__(self, customer: Customer, expedition_reservation: ExpeditionWindow, gear_requests: list[GearRequest], created_at: str, status: ReservationStatus = ReservationStatus.PENDING, reservation_id:str = ""):
        self.__id = "reservation" + str(id(self))
        self.__customer = customer
        self.__expedition_reservation = expedition_reservation
        self.__gear_requests = []
        for request in gear_requests:
            self.__gear_requests.append(request)
        self.__status = status
        self.__created_at = created_at
        if reservation_id != "":
            self.__id = reservation_id

    def change_status(self, status: ReservationStatus) -> None:
        old_status = self.__status
        self.__status = status
        print(f"The status has been changed from {old_status} to {self.__status}")

    def add_gear_request(self, gear_request: GearRequest):
        if isinstance(gear_request, GearRequest):
            self.__gear_requests.append(gear_request)
            print(f"Add a new gear request: {gear_request}")
        else:
            print(f"{gear_request} is not a GearRequest object")
    
    def to_row(self) -> tuple:
        reservation = (self.__id, self.__customer, self.__expedition_reservation, self.__gear_requests, self.__created_at, self.__status)
        return reservation

    @staticmethod
    def from_row(self, reservation: tuple):
        id, customer, expedition_reservation, gear_requests, created_at, status = reservation
        return Reservation(customer, expedition_reservation, gear_requests, created_at, status, id)

    @property
    def id(self):
        return self.__id    

