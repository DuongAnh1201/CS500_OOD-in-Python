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
        #The programs the college offers. Applications share these objects instead of making their own -> Aggregation
        self.__program_list: list[Program] = []

    @property
    def program_list(self) -> list[Program]:
        return self.__program_list

    #The system does not build the Program, it is handed one that already exists -> Aggregation
    def add_program(self, program: Program) -> None:
        if isinstance(program, Program):
            self.__program_list.append(program)
        else:
            print("Wrong type of object, can't add a new program")

    #Show the programs offered and give back the one that is picked, so no new Program is created
    def choose_a_program(self) -> Program|None:
        if len(self.__program_list) == 0:
            print("There is no program offered at the moment")
            return None
        while True:
            print("The programs offered are:")
            for i in range(len(self.__program_list)):
                print(f"  {i + 1}. {self.__program_list[i].program_name}")
            choice = input("Your choice: ").strip()
            if choice.isdigit() and 1 <= int(choice) <= len(self.__program_list):
                return self.__program_list[int(choice) - 1]
            print("That is not one of the programs, please try again")

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

    '''Find one application by its ID and let the user change it through a menu.'''
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
                #Pick one of the programs offered, the application does not get a Program of its own
                new_program = self.choose_a_program()
                if new_program is not None:
                    found_application.change_program(new_program)

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

    #Delete one application from the system by its ID
    def delete(self, application_id: int) -> None:
        f: bool = False
        for i in range(len(self.__application_list)):
            if self.__application_list[i].application_id == application_id:
                self.__application_list[i], self.__application_list[-1] = self.__application_list[-1], self.__application_list[i]
                self.__application_list.pop()
                print(f"Successfully deleted the application with ID: {application_id}")
                f = True
                break
        if f == False:
            print(f"We can't find any application with ID: {application_id}")

    def display(self) -> None:
        print(self)


class UserInterface:
    PROGRAMS_OFFERED = (
        "Computer Science",
        "Data Science",
        "Business Administration",
        "Electrical Engineering",
    )

    def __init__(self) -> None:
        self.__system = ApplicationSystem()
        for program_name in UserInterface.PROGRAMS_OFFERED:
            self.__system.add_program(Program(program_name))

    def __ask_for_a_number(self, question: str) -> int:
        while True:
            answer = input(question)
            if answer.isdigit():
                return int(answer)
            print("Please type a number")

    def run(self) -> None:
        print("=" * 55)
        print("       ADMISSION APPLICATION SYSTEM (ADMIN)")
        print("=" * 55)
        while True:
            print("\n---------------- ADMIN MENU ----------------")
            print("1. Fill in a new admission application form")
            print("2. Show all the applications")
            print("3. Search the applications")
            print("4. Update an application")
            print("5. Delete an application")
            print("0. Exit")
            choice = input("Your choice: ")
            if choice == "1":
                self.add_application()
            elif choice == "2":
                self.__system.display()
            elif choice == "3":
                self.search_applications()
            elif choice == "4":
                application_id = self.__ask_for_a_number("The application ID to update: ")
                self.__system.update(application_id)
            elif choice == "5":
                application_id = self.__ask_for_a_number("The application ID to delete: ")
                self.__system.delete(application_id)
            elif choice == "0":
                print("Goodbye")
                break
            else:
                print("That is not one of the choices, please try again")

    def add_application(self) -> None:
        print("\n" + "=" * 55)
        print("           ADMISSION APPLICATION FORM")
        print("=" * 55)

        print("\nApplicant Information")
        full_name = input("Full Name: ")
        contact_number = input("Contact Number: ")
        email_address = input("Email Address: ")
        address = input(" Address: ")

        print("\nProgram Applied For")
        #The applicant picks one of the programs the college offers -> Aggregation
        program_applied = self.__system.choose_a_program()
        application = Application(
            full_name, contact_number, email_address, address, program_applied
        )

        print("\nPrevious Education (can add multiple entries)")
        print("  Press Enter on the institution when there are no more entries")
        entry_number = 1
        while True:
            print(f"  {entry_number}.")
            institution = input("Institution: ")
            if institution == "":
                break
            degree = input("Degree/Level: ")
            year_completed = self.__ask_for_a_number("Year Completed: ")
            application.add_prev_edu(institution, degree, year_completed)
            entry_number += 1

        print("\nExtracurricular Activities (can add multiple entries)\n")
        print(" Press Enter on the activity name when there are no more entries")
        entry_number = 1
        while True:
            print(f"  {entry_number}.")
            activity_name = input("Activity Name: ")
            if activity_name == "":
                break
            description = input("Description: ")
            application.add_extracurricular(activity_name, description)
            entry_number += 1

        print("\nApplication Status (Admin Use Only)")
        for status in ApplicationStatus:
            print(f"  - {status.name}")
        answer = input("  Status (press Enter to leave it PENDING): ").upper()
        if answer != "":
            chosen_status = None
            for status in ApplicationStatus:
                if status.name == answer:
                    chosen_status = status
                    break
            if chosen_status is None:
                print(f"  {answer} is not one of the statuses, the application stays PENDING")
            else:
                application.update_status(chosen_status)

        print()
        signature = input("Signature of Applicant: ")
        date = input("Date: ")
        self.__system.add(application)
        print("\n" + "-" * 55)
        print("The application has been filed:")
        print(application)
        print(f"Signature of Applicant: {signature}")
        print(f"Date: {date}")
        print("-" * 55)


    def search_applications(self) -> None:
        print("\nSearch the applications, press Enter to skip a criterion")
        applicant_name = input("  Applicant name: ")
        program_applied = input("  Program applied for: ")
        prev_edu = input("  Previous education institution: ")
        results = self.__system.search(
            applicant_name if applicant_name != "" else None,
            program_applied if program_applied != "" else None,
            prev_edu if prev_edu != "" else None,
        )
        for application in results:
            print(application)

def main():
    UserInterface().run()

if __name__ == "__main__":
    main()
