class Person:
    def __init__(self, first_name: str, last_name: str, age: int, phone: str, person_id: str = ""):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__age = age
        self.__phone = phone
        self.__id = "person" + str(id(self))
        # keep the saved ID when the object is loaded back from the database
        if person_id != "":
            self.__id = person_id

    def to_row(self) -> tuple:
        person = (self.__id, self.__first_name, self.__last_name, self.__age, self.__phone)
        return person

    @staticmethod
    def from_row(person: tuple):
        id, first_name, last_name, age, phone = person
        return Person(id, first_name, last_name, age, phone)

    @property
    def id(self):
        return self.__id

    @property
    def first_name(self):
        return self.__first_name

    @property
    def last_name(self):
        return self.__last_name

    @property
    def age(self):
        return self.__age

    @property
    def phone(self):
        return self.__phone

    def __str__(self) -> str:
        return f"ID: {self.__id}\nfirst_name: {self.__first_name}\nlast_name: {self.__last_name}\nage:{self.__age}\nphone:{self.__phone}"
    
class Guide(Person):
    def __init__(self, id, first_name: str, last_name: str, age: int, phone: str, certified: str, technical_skills: dict[str, str], daily_avail: list[str]) -> None:
        super().__init__(first_name, last_name, age, phone, id)
        self.__certified = certified
        self.__technical_skills = {}
        for skill, level in technical_skills.items():
            self.__technical_skills[skill] = level
        self.__daily_avail = []
        for date in daily_avail:
            self.__daily_avail.append(date)

    @property
    def certified(self):
        return self.__certified

    @property
    def technical_skills(self):
        return self.__technical_skills

    @property
    def daily_avail(self):
        return self.__daily_avail

    def add_technical_skill(self, skill: str, level: str) -> None:
        self.__technical_skills[skill] = level
        print(f"Add a new technical skill successfully")

    def add_availability(self, avail: str) -> None:
        if avail not in self.__daily_avail:
            self.__daily_avail.append(avail)
            print(f"Add a new daily availability successfully")
        else:
            print(f"The daily availability is existed")

    def remove_technical_skill(self, skill) -> None:
        if skill in self.__technical_skills: 
            del self.__technical_skills[skill]
            print(f"Remove skill {skill} successfully")
        else:
            print(f"skill {skill} is not in the list yet")

    def remove_availability(self, avail) -> None:
        if avail in self.__daily_avail:
            self.__daily_avail.remove(avail)
            print(f"Remove {avail} successfully")
        else:
            print(f"{avail} is not in the availability list")

    def get_skill_level(self, skill) -> str | None:
        level = None
        if skill in self.__technical_skills:
            level = self.__technical_skills[skill]
        return level

    def is_avail(self, date: str) -> bool:
        if date in self.__daily_avail:
            return True
        return False

    def to_row(self) -> tuple:
        guide = (self.id, self.first_name, self.last_name, self.age, self.phone, self.certified, self.technical_skills, self.daily_avail)
        return guide

    @staticmethod
    def from_row(guide):
        id, first_name, last_name, age, phone, certified, technical_skills, daily_avail = guide
        return Guide(id, first_name, last_name, age, phone, certified, technical_skills, daily_avail)
    
    @staticmethod
    def convert_list(daily_avail: list[str]) -> str:
        return ",".join(daily_avail)

    @staticmethod
    def convert_string(daily_avail: str) -> list[str]:
        dates = []
        if daily_avail != "":
            for date in daily_avail.split(","):
                dates.append(date)
        return dates
    
    def __str__(self) -> str:
        return super().__str__() + f"\ncertified: {self.__certified}\ntechnical_skills: {self.__technical_skills}\ndaily_avail: {self.__daily_avail}"

class Customer(Person):
    def __init__(self, first_name: str, last_name: str, age: int, phone: str, email: str, person_id: str = "") -> None:
        super().__init__(first_name, last_name, age, phone, person_id)
        self.__email = email

    def to_row(self) -> tuple:
        customer = (self.id, self.first_name, self.last_name, self.age, self.phone, self.__email)
        return customer

    @staticmethod
    def from_row(customer: tuple):
        id, first_name, last_name, age, phone, email = customer
        return Customer(first_name, last_name, age, phone, email, id)

    def __str__(self) -> str:
        return super().__str__() + f"\nemail: {self.__email}"




        