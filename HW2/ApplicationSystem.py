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
    @full_name.setter
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
    
    id_counter = 0
    def __init__(self, activity_name: str, description:str = ""):
        Extracurricular.id_counter += 1
        self.__extracurricular_id = Extracurricular.id_counter
        self.__activity_name = activity_name
        self.__description = description

    @property
    def extracurricular_id(self) -> int:
        return self.__extracurricular_id
    def __str__(self) -> str:
        return f"Activity name: {self.__activity_name}\nDescription: {self.__description}"

class PreviousEducation:

    id_counter = 0
    def __init__(self, institution: str, degree: str, year_completed: int) -> None:
        PreviousEducation.id_counter += 1
        self.__prev_edu_id = PreviousEducation.id_counter
        self.__institution = institution
        self.__degree = degree
        self.__year_completed = year_completed
    @property
    def prev_edu_id(self) -> int:
        return self.__prev_edu_id
    @property
    def institution(self) -> str:
        return self.__institution
    @property
    def degree(self) -> str:
        return self.__degree
    @property
    def year_completed(self) -> int:
        return self.__year_completed
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
    id_counter = 0
    def __init__(self, full_name: str, contact_number: str, email_address: str, address: str, program_applied: Program):
        Application.id_counter += 1
        self.__application_id = Application.id_counter
        self.__applicant = Applicant(full_name, contact_number, email_address, address)
        self.__program_applied = program_applied
        self.__status = ApplicationStatus.PENDING
        self.__extracurricular_list: list[Extracurricular] = []
        self.__previous_education_list: list[PreviousEducation] = []

 
    @property
    def application_id(self) -> int:
        return self.__application_id
    @property
    def applicant(self) -> Applicant:
        return self.__applicant
    @property
    def program_applied(self) -> Program:
        return self.__program_applied
    @property
    def status(self) -> ApplicationStatus:
        return self.__status
    @property
    def extracurricular_list(self) -> list[Extracurricular]:
        
        return self.__extracurricular_list
    @property
    def previous_education_list(self) -> list[PreviousEducation]:
        return self.__previous_education_list

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

    def change_program(self, new_program: Program):
        self.__program_applied = new_program
        print("Update program applied")

    def update_status(self, new_status: ApplicationStatus):
        self.__status = new_status
        print("New status is updated")

class ApplicationSystem:
    def __init__(self) -> None:
        self.__application_list: list[Application] = []

    def __str__(self) -> str:
        output = "The Application System includes those Application: \n"
        for application in self.__application_list:
            output += f"{application}"
        return output
        
    def add(self, application: Application) -> None:
        if isinstance(application, Application):
            self.__application_list.append(application)
            print("Adding a new application successfully")
        else:
            print("Wrong type of object, can't add a new application")

    def search(self, applicant_name: str|None = None, program_applied: str|None = None, prev_edu: str|None = None ) -> list[Application]:
        results: list[Application] = []
        for application in self.__application_list:
            if applicant_name is not None and application.applicant.full_name != applicant_name:
                continue
            if program_applied is not None and application.program_applied.program_name != program_applied:
                continue
            #Add every application that has a record from the same previous education
            if prev_edu is not None:
                for record in application.previous_education_list:
                    if record.institution == prev_edu:
                        results.append(application)
                        break
            else:
                results.append(application)

        print(f"Found {len(results)} application(s) for the search")
        return results

    '''Find one application by its ID and let the user change it through a menu.
       Every change goes through the methods of Application, so the Application keeps looking after its own data.'''
    def update(self, application_id: int) -> None:
        found_application: Application|None = None
        for application in self.__application_list:
            if application.application_id == application_id:
                found_application = application
                break

        #Handle an ID that is not in the system instead of crashing
        if found_application is None:
            print(f"We can't find any application with ID: {application_id}")
            return

        print(f"Updating the application with ID: {application_id}")
        while True:
            print("\nWhat do you want to update?")
            print("1. Change the program applied for")
            print("2. Update the application status")
            print("3. Add an extracurricular activity")
            print("4. Remove an extracurricular activity")
            print("5. Add a previous education record")
            print("6. Remove a previous education record")
            print("7. Show the application")
            print("0. Finish updating")
            choice = input("Your choice: ")

            if choice == "1":
                new_program = input("The new program name: ")
                found_application.change_program(Program(new_program))

            elif choice == "2":
                print("The statuses are:")
                for status in ApplicationStatus:
                    print(f"- {status.name}")
                new_status = input("The new status: ").upper()
                chosen_status = None
                for status in ApplicationStatus:
                    if status.name == new_status:
                        chosen_status = status
                        break
                if chosen_status is None:
                    print(f"{new_status} is not one of the statuses")
                else:
                    found_application.update_status(chosen_status)

            elif choice == "3":
                activity_name = input("The activity name: ")
                description = input("The description: ")
                found_application.add_extracurricular(activity_name, description)

            elif choice == "4":
                #Show what is there, so the user knows which ID to type
                print("The extracurricular activities are:")
                for extracurricular in found_application.extracurricular_list:
                    print(f"- ID {extracurricular.extracurricular_id}: {extracurricular}")
                extracurricular_id = input("The ID to remove: ")
                
                found_application.remove_extracurricular(int(extracurricular_id))

            elif choice == "5":
                institution = input("The institution: ")
                degree = input("The degree: ")
                year_completed = input("The year completed: ")
                if year_completed.isdigit():
                    found_application.add_prev_edu(institution, degree, int(year_completed))
                else:
                    print("The year has to be a number")

            elif choice == "6":
                print("The previous education records are:")
                for record in found_application.previous_education_list:
                    print(f"- ID {record.prev_edu_id}: {record}")
                prev_edu_id = input("The ID to remove: ")
                found_application.remove_prev_edu(int(prev_edu_id))
            
            elif choice == "7":
                print(found_application)

            elif choice == "0":
                print(f"Finished updating the application with ID: {application_id}")
                break

            else:
                print("That is not one of the choices, please try again")


def main():
    print("========== Creating an application ==========")
    computer_science = Program("Computer Science")
    application = Application(
        "Ann Lee", "555-0100", "ann@example.com", "1 Main St", computer_science
    )
    print(application)

    print("========== Adding extracurricular activities ==========")
    #The application creates the Extracurricular objects itself, it is not handed ready-made ones
    application.add_extracurricular("Robotics Club", "Participated in robotics competitions")
    application.add_extracurricular("Chess Team", "Played in regional tournaments")
    application.add_extracurricular("Debate Club", "Practiced public speaking")

    print("\n========== Adding previous education records ==========")
    application.add_prev_edu("City College", "Associate Degree", 2021)
    application.add_prev_edu("Lincoln High School", "High School Diploma", 2018)

    print("\n========== The application so far ==========")
    print(application)

    print("========== Removing an extracurricular and a previous education ==========")
    application.remove_extracurricular(2)
    application.remove_prev_edu(2)

    print("\n========== Removing records that are not there ==========")
    application.remove_extracurricular(99)
    application.remove_prev_edu(99)

    print("\n========== Changing the program and the status ==========")
    application.change_program(Program("Data Science"))
    application.update_status(ApplicationStatus.ACCEPTED)

    print("\n========== The final application ==========")
    print(application)

    print("========== Putting three applications into the system ==========")
    system = ApplicationSystem()
    system.add(application)

    bob = Application("Bob Tran", "555-0199", "bob@example.com", "2 Oak Ave", Program("Data Science"))
    bob.add_prev_edu("City College", "Associate Degree", 2020)
    system.add(bob)

    cara = Application("Cara Diaz", "555-0123", "cara@example.com", "3 Pine Rd", Program("Data Science"))
    cara.add_prev_edu("SFBU", "BSc Computer Science", 2023)
    system.add(cara)

    print("\n========== Searching by applicant name ==========")
    for found in system.search(applicant_name="Bob Tran"):
        print(found)

    print("========== Searching by program applied for ==========")
    for found in system.search(program_applied="Data Science"):
        print(found)

    print("========== Searching by previous education ==========")
    for found in system.search(prev_edu="City College"):
        print(found)

    print("========== Searching by several criteria at once ==========")
    for found in system.search(program_applied="Data Science", prev_edu="SFBU"):
        print(found)

    print("========== Searching for something that is not there ==========")
    system.search(applicant_name="Nobody At All")

    print("\n========== Updating an application that is not in the system ==========")
    system.update(99)

    #This one is interactive, so it is the last thing main does. Answer 0 to finish.
    print("\n========== Updating the application with ID 2 ==========")
    system.update(2)


if __name__ == "__main__":
    main()
