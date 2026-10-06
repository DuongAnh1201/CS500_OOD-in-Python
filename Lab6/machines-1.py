from abc import ABC, abstractmethod

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
    def partno(self) -> int:
        return self.__partno

    @property
    def price(self) -> float:
        return self.__price

    def display(self) -> None:
        print(self)

class MovablePart(Part, Movable):
    def __init__(self, partno: int, price: float, type: str) -> None:
        super().__init__(partno, price)
        self.__type = type
    def __str__(self) -> str:
        return super().__str__() + f"\ntype = {self.__type}"
    def display(self) -> None:
        print(self)
    @property
    def type(self) -> str:
        return self.__type
    def move(self) -> None:
        print(f"partno: {self.partno} is moving fast!")

class Machine(Displayable):
    def __init__(self, machine_name: str) -> None:
        self.__machine_name = machine_name
        self.__parts: list[Part] = []

    @property
    def machine_name(self) -> str:
        return self.__machine_name

    def __iter__(self):
        return iter(self.__parts)

    def add_part(self, part: Part) -> None:
        self.__parts.append(part)

    def __str__(self) -> str:
        output = f"machine_name = {self.__machine_name}\nThe machine has these parts:\n"
        for part in self.__parts:
            output += str(part) + "\n\n"
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
    def __init__(self, machine_name: str, processor: str, model: str, speed: int) -> None:
        Machine.__init__(self, machine_name)
        JetFighter.__init__(self, model, speed)
        self.__processor = processor

    def dowork(self) -> None:
        print(f"The Robot {self.machine_name} is assembling a big truck.")

    def fly(self) -> None:
        JetFighter.fly(self)
        print(f"The Robot {self.machine_name} is flying over the ocean!")

    def get_expensive_parts(self, priceLimit: float) -> list[Part]:
        expen_part = []
        for part in self:
            if part.price>= priceLimit:
                expen_part.append(part)
        return expen_part


    def get_movable_parts_bytype(self) -> dict[str, list[MovablePart]]:
        movable_parts = {}
        for part in self:
            if isinstance(part, MovablePart):
                if part.type not in movable_parts:
                    movable_parts[part.type] = [part]
                else:
                    movable_parts[part.type].append(part)
        return movable_parts

    def get_movable_parts(self) -> list[MovablePart]:
        movable_parts = []
        for part in self:
            if isinstance(part, MovablePart):
                movable_parts.append(part)
        return movable_parts

    def __str__(self) -> str:
        return f"processor = {self.__processor}\n" + Machine.__str__(self) + JetFighter.__str__(self)

    def display(self) -> None:
        print(self)

def main():
    robo = Robot('MTX', 'M1X', 'F-16', 10000)
    robo.add_part(Part(111, 100))
    robo.add_part(Part(222, 200))
    robo.add_part(Part(333, 300))
    robo.add_part(Part(222, 300))
    robo.add_part(MovablePart(555, 300, "TypeA"))
    robo.add_part(Part(111, 100))
    robo.add_part(Part(111, 100))
    robo.add_part(MovablePart(777, 300, "TypeB"))
    robo.add_part(MovablePart(655, 300, "TypeA"))
    robo.add_part(MovablePart(755, 300, "TypeA"))
    robo.add_part(MovablePart(977, 300, "TypeB"))
    robo.display()
    print()

    print("\nRobot test flight----")
    robo.fly()
    print("\nRobot dowork() test ----")
    robo.dowork()

    print("\nDuplicated part list----")
    partfreq = robo.get_duplicated_parts()
    for partno in partfreq.keys():
        print(partno,'=>', partfreq[partno], 'times')

    print("\nExpensive part list----")
    expensive_parts = robo.get_expensive_parts(200)
    for part in expensive_parts:
        part.display()

    print("\nMovable part list----")
    movable_parts = robo.get_movable_parts_bytype()
    for type, parts in movable_parts.items():
        print("type =", type)
        for part in parts:
            part.display()
        print()

    print("\nAsk movable to move----")
    movable_parts = robo.get_movable_parts()
    for part in movable_parts:
        part.move()

    print("\nTest remove_part() ----")
    robo.remove_part_by_partno(333)
    for part in robo:
        if part.partno == 333:
            print('Found 333')
            break


if __name__ == "__main__":
    main()
