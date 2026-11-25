from abc import ABC, abstractmethod
from enum import Enum
class Repository(ABC):
    @abstractmethod
    def save(self):
        pass

    @abstractmethod
    def find_by_id(self, obj_id):
        pass

    @abstractmethod
    def find_all(self) -> list:
        pass

    @abstractmethod
    def update(self) -> None:
        pass

    @abstractmethod
    def delete(self, obj_id) -> None:
        pass

class BaseRegistry(ABC):
    @abstractmethod
    def add(self, obj):
        pass

    @abstractmethod
    def get_by_id(self, obj_id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def update(self, obj):
        pass

    @abstractmethod
    def delete(self, obj_id):
        pass
    
class ReservationStatus(Enum):
    PENDING = "pending"
    CONFIRMED = "confirmed"
    CANCEL = "cancelled"
    COMPLETED = "completed"

class GearRequestStatus(Enum):
    PENDING = "pending" 
    APPROVED = "approved"
    REJECTED = "rejected"
