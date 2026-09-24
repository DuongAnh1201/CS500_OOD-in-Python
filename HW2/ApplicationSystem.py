from enum import Enum

class Applicant:
    def __init__(self, full_name: str, contact_number: str, email_address: str, address: str):
        self.__full_name = full_name
        self.__contact_number = contact_number
        self.__email_address = email_address
        self.__address = address
    @property
    def full_name(self) -> str:
        return self.__full_name
    full_name.setter
    def full_name(self, new_full_name: str) -> None:
        self.__full_name = new_full_name
    @property
    def contact_number(self) -> str:
        return self.__contact_number
    @contact_number.setter
    def contact_number(self, new_contact_number: str) -> None:
        self.__contact_number = new_contact_number
    @property
    def email_address(self) -> str:
        return self.__email_address
    @email_address.setter
    def email_address(self, new_email_address: str) -> None:
        self.__email_address = new_email_address
    @property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, new_address: str) -> None:
        self.__address = new_address
    

    def __str__(self):
        return f"Full name: {self.__full_name}\nContact number: {self.__contact_number}\nEmail address: {self.__email_address}\nAddress: {self.__address}"

class ApplicationStatus(Enum):
    PENDING = 0
    REVIEWED = 1 
    REJECTED = 2
    ACCEPTED = 3

class Extracurricular:
    extracurricular_id = 0
    def __init__(self, activity_name: str, description:str = ""):
        extracurricular_id += 1
        self.__extracurricular_id = extracurricular_id
        self.__activity_name = activity_name
        self.__description = description

    @property
    def extracurricular_id(self) -> int:
        return self.__extracurricular_id
    def __str__(self) -> str:
        return f"Activity name: {self.__activity_name}\nDescription: {self.__description}"

class PreviousEducation:
    prev_edu_id = 0
    def __init__(self, institution: str, degree: str, year_completed: int) -> None:
        prev_edu_id += 1
        self.__prev_edu_id = prev_edu_id
        self.__institution = institution
        self.__degree = degree
        self.__year_completed = year_completed
    @property
    def prev_edu_id(self) -> int:
        return self.__prev_edu_id
    def __str__(self) -> str:
        return f"Institution: {self.__institution}\nDegree/Level: {self.__degree}\nYear completed: {self.__year_completed}\n"

class Program:
    def __init__(self, program_name: str) -> None:
        self.__program_name = program_name

    @property
    def program_name(self) -> str:
        return self.__program_name
    def __str__(self) -> str:
        return f"Program: {self.__program_name}\n"

class Application:
    application_id = 0
    def __init__(self, full_name: str, contact_number: str, email_address: str, address: str, program_applied: Program):
        application_id += 1
        self.__application_id = application_id
        self.__applicant = Applicant(full_name, contact_number, email_address, address)
        self.__program_applied = program_applied
        self.__status = ApplicationStatus.PENDING
        self.__extracurricular_list: list[Extracurricular] = []
        self.__previous_education_list: list[PreviousEducation] = []

    def __str__(self) -> str:
        output = ""
        output += f"Application_id: {self.__application_id}\nApplicant: {self.__applicant}\nProgram Applied: {self.__program_applied}\nApplication status: {self.__status}\n"
        output += ("\nThe Applicant has the following extracurricular: \n")
        for extracurricular in self.__extracurricular_list:
            output += f"{extracurricular}\n"

        output += ("\nThe Applicant has the Previous Education: \n")
        for prev_edu in self.__previous_education_list:
            output+= f"{prev_edu}\n"
        return output

    ''' Implementing the methods defined in the UML for adding and removing extracurricular activities aswsociated with an application -> Composition'''
    def add_extracurricular(self, activity_name: str, description: str) -> None:
        extracurricular = Extracurricular(activity_name, description)
        self.__extracurricular_list.append(extracurricular)
        print(f"New extracurricular: {extracurricular} has been added")

    #Remove an extracurricular by its ID
    def remove_extracurricular(self, extracurricular_id):
        f: bool = False
        for i in range(len(self.__extracurricular_list)):
            if self.__extracurricular_list[i].extracurricular_id == extracurricular_id:
                self.__extracurricular_list[i], self.__extracurricular_list[-1] = self.__extracurricular_list[-1], self.__extracurricular_list[i]
                self.__extracurricular_list.pop()
                print(f"Successfully removed the extracurricular with ID: {extracurricular_id}")
                f = True
                break
        if f == False:
            print(f"We can't find any curricular with ID: {extracurricular_id}")

    '''Implementing the methods defined in the UML for adding and removing Previous Education Management associated with an application -> Composition'''
    def add_prev_edu(self, institution: str, degree: str, year_completed: int) -> None:
        prev_edu = PreviousEducation(institution, degree, year_completed)
        self.__previous_education_list.append(prev_edu)
        print(f"New previous education: {prev_edu} has been added")

    #Remove a previous education by its ID
    def remove_prev_edu(self, prev_edu_id):
        f: bool = False
        for i in range(len(self.__previous_education_list)):
            if self.__previous_education_list[i].prev_edu_id == prev_edu_id:
                self.__previous_education_list[i], self.__previous_education_list[-1] = self.__previous_education_list[-1], self.__previous_education_list[i]
                self.__previous_education_list.pop()
                print(f"Successfully removed the previous education with ID: {prev_edu_id}")
                f = True
                break
        if f == False:
            print(f"We can't find any previous education with ID: {prev_edu_id}")
