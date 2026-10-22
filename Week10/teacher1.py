
class Teacher:
    def __init__(self, name: str) -> None:
        self.name = name

    def create_assignment(self, assignment: str):
        print(f"Teacher {self.name} created assignment {assignment}")

class Student:
    def __init__(self, name: str) -> None:
        self.name = name

    def do_assignment(self, assignment: str):
        print(f"Student {self.name} is doing assignment {assignment}")


class Dean:
    def __init__(self, name: str) -> None:
        self.name = name

    def review_assignment(self, assignment: str):
        print(f"Dean {self.name} is review assignment {assignment}")


def main():
    t = Teacher("Henry")
    s1 = Student("Peter")
    s2 = Student("Nancy")
    s3 = Student("Lily")
    d = Dean("Dave")
    
    t.create_assignment("HW1")
    s1.do_assignment("HW1")
    s2.do_assignment("HW1")
    s3.do_assignment("HW1")
    d.review_assignment("HW1")
    print()
    t.create_assignment("HW2")

if __name__ == "__main__":
    main()
