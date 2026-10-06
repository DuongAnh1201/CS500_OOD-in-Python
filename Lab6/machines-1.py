from abc import ABC, abstractmethod, abstractproperty

class Movable(ABC):
    @abstractmethod
    def move(self) -> None:
        pass

class Displayable(ABC):
    @abstractmethod
    def display(self) -> None:
        pass

class Flyable(ABC):
    @abstractmethod
    def fly(self) -> None:
        pass

class Part(Displayable):
    def __init__(self, partno: int, price: float) -> None:
        self.__partno = partno
        self.__price = price

    def __str__(self) -> str:
        return f"partno = {self.__partno}\nprice = {self.__price}"
    
    @property
    def partno(self):
        return self.__partno
    def display(self) -> None:
        print(self)

    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Part):
            return self.__partno == __value.__partno
        else:
            return False

class MovablePart(Part, Movable):
    def __init__(self, partno, price, type) -> None:
        Part.__init__(partno, price)
        self.__type = type
    def __str__(self) -> str:
        return Part.__str__() + f"\nType: {self.__type}"
    def display(self) -> None:
        print(self)
    @property
    def type(self):
        return self.__type
    def move(self):
        print(f"partno: {Part.partno} is moving fast!")

class Machine(Displayable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    @property
    def parts(self) -> list:
        return self.__parts

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __str__(self) -> str:
        output = f"Machine name: {self.__machine_name}"
        for part in self.__parts:
            output += part + "\n"
        return output

    def display(self) -> None:
        print(self)

    @abstractmethod
    def dowork(self) -> None:
        pass

    def remove_part_by_partno(self, partno:int) -> None:
        i = 0
        while i< len(self.__parts):
            if partno==self.__parts[i].partno:
                self.__parts.pop(i)
            else:
                i+=1

    def get_duplicated_parts(self) -> dict[int, int]:
        counters: dict[int, int] = {}
        for part in self.__parts:
            if part.partno in counters:
                counters[part.partno] += 1
            else:
                counters[part.partno] = 1
        result: dict[int, int] = {}
        for partno, occurences, in counters.items():
            if occurences > 1:
                result[partno] = occurences
        return result


class JetFighter(Displayable, Flyable):
    def __init__(self, model: str, speed: int) -> None:
        self.__model = model
        self.__speed = speed

    def __str__(self) -> str:
        return f"model = {self.__model}\nspeed = {self.__speed}"
    
    def display(self) -> None:
        print(self)

    def fly(self) -> None:
        print(f"The JetFigher {self.__model} is flying in the sky!")

class Robot(Machine, JetFighter):
    def __init__(self, machine_name: str, cpu: str, model: str, speed: int, processor: str) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__processor = processor

    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None:
        JetFighter.fly(self)

    def get_expensive_parts(self, priceLimit: float) -> list[Part]:
        expen_part = []
        for part in Machine.parts:
            if part.price>= priceLimit:
                expen_part.append(part)
        return expen_part


    def get_movable_parts_bytype(self) -> dict[str, list[Part]]:
        movable_parts = {}
        for part in Machine.parts:
            if isinstance(part, MovablePart):
                if part.type not in movable_parts:
                    movable_parts[part.type] = [part]
                else:
                    movable_parts[part.type].append(part)
        return movable_parts

    def get_movable_parts(self) -> list[MovablePart]:
        movable_parts = []
        for part in Machine.parts:
            if isinstance(part, MovablePart):
                movable_parts.append(part)
        return movable_parts

    def __str__(self) -> str:
        return super().__str__() + f"\nProcessor: {self.__processor}"
    
    def display(self) -> None:
        print(self)

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))


if __name__ == "__main__":
    main()