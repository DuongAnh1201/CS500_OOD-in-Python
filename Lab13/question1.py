from abc import ABC, abstractmethod
#Target Interface
class FirstSystem(ABC):
    @abstractmethod
    def foo(self, a: int) -> str:
        pass

#Adaptee
class SecondSystem:
    def bar(self, b: str) -> int:
        return int(b)

#Adapter
class Adapter(FirstSystem):
    def __init__(self, obj : SecondSystem) -> None:
        self.__obj = obj

    def foo(self, a: int) -> str:
        return str(self.__obj.bar(str(a)))

class Factory:
    @staticmethod
    def create_system() -> FirstSystem:
        return Adapter(SecondSystem())

def main():
    system = Factory.create_system()
    print("Result: ", system.foo(12345))


if __name__ == "__main__":
    main()

    
