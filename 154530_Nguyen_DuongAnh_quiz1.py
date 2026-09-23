class Professor:
    def __init__(self, name: str, senior: bool) -> None:
        self.__name = name
        self.__senior = senior

    @property
    def senior(self):
        return self.__senior
    def __str__(self) -> str:
        return f"Professor: {self.__name}\nSenior: {self.__senior}\n"


class Building:
    def __init__(self, buildingName: str) -> None:
        self.__buildingName: str = buildingName
        self.__stories = 10

    def __str__(self) -> str:
        return f"Building: {self.__buildingName}\nStories: {self.__stories}\n"

class Department:
    def __init__(self, deptName: str, building: str) -> None:
        self.__deptName: str = deptName
        self.__building: Building = Building(building)
        self.__professors: list[Professor] = []

    @property
    def deptName(self):
        return self.__deptName
    def __str__(self) -> str:
        output = f"Department: {self.__deptName}\n{self.__building}"
        output += "\nThe department has following professors: "
        for professor in self.__professors:
            output += f"\n{professor}\n"
        return output

    def addProfessor(self, prof: Professor):
        if isinstance(prof, Professor):
            self.__professors.append(prof)

    def getSeniorProfessors(self) -> list:
        senior_professor: list = []
        for professor in self.__professors:
            if professor.senior:
                senior_professor.append(professor)
        return senior_professor

def main():
    p1 = Professor("Ken", True)
    p2 = Professor("Peter", True)
    p3 = Professor("Robin", False)
    p4 = Professor("Tom", False)
    depart = Department("Engineering", "Main Building")
    depart.addProfessor(p1)
    depart.addProfessor(p2)
    depart.addProfessor(p3)
    depart.addProfessor(p4)
    print("Professor testing: ")
    print(p1)
    print(p2)
    print(depart)
    senior_professors = depart.getSeniorProfessors()
    print(f"The department {depart.deptName} has the following senior professors: \n")
    for professor in senior_professors:
        print(professor)
if __name__ == "__main__":
    main()