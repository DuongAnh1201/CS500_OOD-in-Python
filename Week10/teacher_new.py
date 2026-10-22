from abc import ABC, abstractmethod
from operator import methodcaller

class Observer(ABC):
    @abstractmethod
    def update(self, date):
        pass

class Subject(ABC):
    @abstractmethod
    def subscribe(self, obs: Observer):
        pass

    @abstractmethod
    def unsubscribe(self, obs: Observer):
        pass

    @abstractmethod
    def notiy(self, data):
        pass

class Teacher(Subject):
    def __init__(self, name: str) -> None:
        self.name = name
        self.__observers: list[Observer]

    def subscribe(self, obs: Observer):
        self.__observers.append(obs)

    def unsubscribe(self, obs: Observer):
        self.__observers.remove(obs)

    def notify(self, data):
        for o in self.__observers:
            o.update(data)

    def create_assignment(self, assignment: str):
        print(f"Teacher {self.name} created assignment {assignment}")

class Student(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def do_assignment(self, assignment: str):
        print(f"Student {self.name} is doing assignment {assignment}")

    def update(self, data):
        self.do_assignment(data)

class Dean(Observer):
    def __init__(self, name: str) -> None:
        self.name = name

    def review_assignment(self, assignment: str):
        print(f"Dean {self.name} is review assignment {assignment}")

    def update(self, data):
        self.review_assignment(data)

def main():
    t = Teacher("Henry")
    s1 = Student("Peter")
    s2 = Student("Nancy")
    s3 = Student("Lily")
    d = Dean("Dave")
    t.subscribe(s1)
    t.subscribe(s2)
    t.subscribe(s3)
    t.subscribe(d)
    t.create_assignment("HW1")

if __name__ == "__main__":
    main()
