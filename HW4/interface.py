from abc import ABC, abstractmethod
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
    
