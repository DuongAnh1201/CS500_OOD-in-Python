class Person:
    def __init__(self, name: str):
        self.__name = name

    def __str__(self) -> str:
        return f"name = {self.__name}"

    def display(self)->None:
        print(self)

    def dowork(self) -> None:
        print("Doing nothing")

    @property
    def name(self) -> str:
        return self.__name

class Programmer(Person):
    def __init__(self, name: str, skills: str, salary: float) -> None:
        super().__init__(name)
        self.__skills = skills
        self.__salary = salary

    def __str__(self):
        return super().__str__()+ f"\nskills = {self.__skills}\nsalary = {self.__salary}"

    def get_annual_income(self) -> float:
        return self.__salary*12

    def dowork(self) -> None:
        print(f"Programmer {self.name} is writing a program")

class Manager(Programmer):
    def __init__(self, name: str, skills: str, salary: float, bonus: float) -> None:
        super().__init__(name, skills, salary)
        self.__bonus = bonus

    def __str__(self):
        return super().__str__() + f"\nbonus = {self.__bonus}"

    def get_annual_income(self) -> float:
        return super().get_annual_income() + self.__bonus

    def dowork(self) ->None:
        print(f"Manager {self.name} is supervising a team of programmer.")

class Group:
    def __init__(self, groupname: str) -> None:
        self.__groupname = groupname
        self.__members: list[Person] = []

    def add_member(self, member: Programmer) -> None:
        self.__members.append(member)

    #Remove all members whose name is same as parameter name
    def remove_member(self, name: str) -> None:
        i = 0
        while i< len(self.__members):
            if self.__members[i].name == name:
                self.__members[i], self.__members[-1] = self.__members[-1], self.__members[i]
                self.__members.pop()
            else:
                i+= 1
        
    def __str__(self) -> str:
        output = "The group has these members: \n"
        for member in self.__members:
            output += member.__str__() + "\n"
        return output

    def display(self) -> None:
        print(self)

    def ask_manager_dowork(self) -> None:
        for member in self.__members:
            if isinstance(member, Manager):
                member.dowork()

    def ask_anyone_dowork(self) -> None:
        for member in self.__members:
            member.dowork()

    def get_allMembers_morethan(self, income: float) -> list[Programmer]:
        result: list[Programmer] = []
        for member in self.__members:
            if member.get_annual_income() > income:
                result.append(member)
        return result
    
class Project:
    def __init__(self, projname: str, budget: float, active: bool) -> None:
        self.__projname = projname
        self.__budget = budget
        self.__active = active

    def __str__(self) -> str:
        return f"Project name: {self.__projname}\nBudget: {self.__budget}\nActive: {self.__active}"

    @property
    def active(self):
        return self.__active
    def display(self) -> str:
        print(self.__str__())
    def __eq__(self, proj):
        if isinstance(proj, Project):
            return self.__budget>proj.__budget

class ITGroup(Group): #Aggregation, many to one relationship with project, is a subclass of the group
    def __init__(self,groupname: str) -> None:
        super().__init__(groupname)
        self.__projects = []
        
    def add_project(self, project) -> None:
        if isinstance(project, Project):
            self.__projects.append(project)

    def find_largest_project(self) -> Project:
        largest: Project | None = None
        for i in self.__projects:
            if largest == None or Project.__eq__(i, largest):
                largest = i
        return largest

    def __str__(self):
        output: str = "\nThe group has these projects: \n"
        for project in self.__projects:
            output += project.__str__() + "\n"
            
        return super().__str__() + output

    def display(self):
        print(self.__str__())

    def get_active_projects(self) -> list[Project]:
        result: list[Project] = []
        for project in self.__projects:
            if project.active:
                result.append(project)
        return result
            


def main() -> None:
    p1: Programmer = Programmer("Lily", "C++, Java", 10000)
    p2: Programmer = Programmer("Judy", "Python, Java", 18000)
    m: Manager = Manager("Peter", "Management", 20000, 20000)
    proj1: Project = Project("MAX-5", 200000, True)
    proj2: Project = Project("FOX-4", 100000, False)
    proj3: Project = Project("FOX-XP", 500000, True)
    itgrp: ITGroup = ITGroup("ATX Group")
    itgrp.add_member(p1)
    itgrp.add_member(p2)
    itgrp.add_member(m)
    itgrp.add_project(proj1)
    itgrp.add_project(proj2)
    itgrp.add_project(proj3)
    itgrp.display()
    p3: Programmer = Programmer("Jone", "Python, Java", 1118000)
    itgrp.add_member(p3)
    itgrp.ask_anyone_dowork()
    print()
    itgrp.ask_manager_dowork()

    print("\nGet the largest project...")
    maxProj: Project|None = itgrp.find_largest_project()
    if maxProj is not None:
        maxProj.display()
    print("\nGet the acive projects...")
    projects: list[Project] = itgrp.get_active_projects()
    for proj in projects:
        proj.display()
    print()
    itgrp.display()
    itgrp.remove_member(p3.name)
    print("\nGet the members with high income...")
    members: list[Programmer] = itgrp.get_allMembers_morethan(200000)
    for member in members:
        member.display()
    print()
if __name__ == "__main__":
    main()