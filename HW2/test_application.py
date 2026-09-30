'''Unit tests for the Application class defined in ApplicationSystem.py

Run them with:
    python3 -m unittest test_application -v
    python3 test_application.py
'''

import io
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

from ApplicationSystem import (
    Application,
    ApplicationStatus,
    ApplicationSystem,
    Extracurricular,
    PreviousEducation,
    Program,
)


def call_quietly(method, *args) -> str:
    '''Call a method, hide what it prints, and give the printed text back so it can be checked'''
    buffer = io.StringIO()
    with redirect_stdout(buffer):
        method(*args)
    return buffer.getvalue()


class TestApplication(unittest.TestCase):
    def setUp(self) -> None:
        #The IDs come from class level counters, so reset them to keep every test independent
        Application.id_counter = 0
        Extracurricular.id_counter = 0
        PreviousEducation.id_counter = 0

        self.program = Program("Computer Science")
        self.application = Application(
            "Ann Lee", "555-0100", "ann@example.com", "1 Main St", self.program
        )

    #The two lists are private, so the tests read them through their name mangled attributes
    def extracurriculars(self) -> list:
        return self.application._Application__extracurricular_list

    def previous_educations(self) -> list:
        return self.application._Application__previous_education_list

    '''Test the creation of an Application object'''
    def test_application_creation(self) -> None:
        output = str(self.application)
        self.assertIn("Application_id: 1", output)
        self.assertIn("Ann Lee", output)
        self.assertIn("Computer Science", output)
        #A brand new application starts as PENDING with nothing attached to it
        self.assertIn("PENDING", output)
        self.assertEqual(self.extracurriculars(), [])
        self.assertEqual(self.previous_educations(), [])

    def test_application_id_increases_for_each_application(self) -> None:
        second = Application(
            "Bob Tran", "555-0199", "bob@example.com", "2 Oak Ave", Program("Data Science")
        )
        self.assertIn("Application_id: 1", str(self.application))
        self.assertIn("Application_id: 2", str(second))

    '''Test __str__()'''
    def test_str_shows_every_part_of_the_application(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        call_quietly(self.application.add_prev_edu, "City College", "Associate Degree", 2021)
        output = str(self.application)

        #The applicant block
        self.assertIn("Full name: Ann Lee", output)
        self.assertIn("Contact number: 555-0100", output)
        self.assertIn("Email address: ann@example.com", output)
        self.assertIn("Address: 1 Main St", output)
        #The program, the status and both headings
        self.assertIn("Program: Computer Science", output)
        self.assertIn("PENDING", output)
        self.assertIn("The Applicant has the following extracurricular:", output)
        self.assertIn("The Applicant has the Previous Education:", output)
        #The records the application owns
        self.assertIn("Activity name: Robotics Club", output)
        self.assertIn("Description: Built a robot", output)
        self.assertIn("Institution: City College", output)
        self.assertIn("Degree/Level: Associate Degree", output)
        self.assertIn("Year completed: 2021", output)

    '''Test add_extracurricular()'''
    def test_add_extracurricular(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")

        self.assertEqual(len(self.extracurriculars()), 1)
        added = self.extracurriculars()[0]
        #The application builds the Extracurricular itself, which is what composition means here
        self.assertIsInstance(added, Extracurricular)
        self.assertEqual(added.extracurricular_id, 1)
        self.assertIn("Activity name: Robotics Club", str(added))

    def test_add_extracurricular_announces_the_new_activity(self) -> None:
        printed = call_quietly(
            self.application.add_extracurricular, "Chess Team", "Regional tournaments"
        )
        self.assertIn("Chess Team", printed)
        self.assertIn("has been added", printed)

    '''Test remove_extracurricular()'''
    def test_remove_extracurricular(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        printed = call_quietly(self.application.remove_extracurricular, 1)

        self.assertEqual(self.extracurriculars(), [])
        self.assertIn("Successfully removed the extracurricular with ID: 1", printed)
        self.assertNotIn("Robotics Club", str(self.application))

    def test_remove_extracurricular_only_removes_the_matching_one(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        call_quietly(self.application.add_extracurricular, "Chess Team", "Regional tournaments")
        call_quietly(self.application.add_extracurricular, "Debate Club", "Public speaking")

        call_quietly(self.application.remove_extracurricular, 2)

        remaining_ids = [item.extracurricular_id for item in self.extracurriculars()]
        self.assertCountEqual(remaining_ids, [1, 3])
        output = str(self.application)
        self.assertIn("Robotics Club", output)
        self.assertIn("Debate Club", output)
        self.assertNotIn("Chess Team", output)

    '''Test add_prev_edu()'''
    def test_add_prev_edu(self) -> None:
        call_quietly(self.application.add_prev_edu, "City College", "Associate Degree", 2021)

        self.assertEqual(len(self.previous_educations()), 1)
        added = self.previous_educations()[0]
        #The application builds the PreviousEducation itself, the same composition as above
        self.assertIsInstance(added, PreviousEducation)
        self.assertEqual(added.prev_edu_id, 1)
        self.assertIn("Institution: City College", str(added))

    def test_add_prev_edu_announces_the_new_record(self) -> None:
        printed = call_quietly(self.application.add_prev_edu, "SFBU", "BSc", 2024)
        self.assertIn("SFBU", printed)
        self.assertIn("has been added", printed)

    '''Test remove_prev_edu()'''
    def test_remove_prev_edu(self) -> None:
        call_quietly(self.application.add_prev_edu, "City College", "Associate Degree", 2021)
        printed = call_quietly(self.application.remove_prev_edu, 1)

        self.assertEqual(self.previous_educations(), [])
        self.assertIn("Successfully removed the previous education with ID: 1", printed)
        self.assertNotIn("City College", str(self.application))

    def test_remove_prev_edu_only_removes_the_matching_one(self) -> None:
        call_quietly(self.application.add_prev_edu, "SFBU", "BSc", 2024)
        call_quietly(self.application.add_prev_edu, "City College", "Associate Degree", 2021)
        call_quietly(self.application.add_prev_edu, "Lincoln High", "Diploma", 2018)

        call_quietly(self.application.remove_prev_edu, 2)

        remaining_ids = [record.prev_edu_id for record in self.previous_educations()]
        self.assertCountEqual(remaining_ids, [1, 3])
        output = str(self.application)
        self.assertIn("SFBU", output)
        self.assertIn("Lincoln High", output)
        self.assertNotIn("City College", output)

    '''Test change_program()'''
    def test_change_program(self) -> None:
        new_program = Program("Data Science")
        call_quietly(self.application.change_program, new_program)

        output = str(self.application)
        self.assertIn("Program: Data Science", output)
        self.assertNotIn("Computer Science", output)

    '''Test update_status()'''
    def test_update_status(self) -> None:
        call_quietly(self.application.update_status, ApplicationStatus.ACCEPTED)
        self.assertIn("ACCEPTED", str(self.application))

    def test_update_status_through_every_stage(self) -> None:
        for status in (
            ApplicationStatus.REVIEWED,
            ApplicationStatus.REJECTED,
            ApplicationStatus.ACCEPTED,
        ):
            call_quietly(self.application.update_status, status)
            self.assertIn(status.name, str(self.application))

    '''Test multiple extracurricular activities'''
    def test_multiple_extracurriculars(self) -> None:
        activities = [
            ("Robotics Club", "Built a robot"),
            ("Chess Team", "Regional tournaments"),
            ("Debate Club", "Public speaking"),
        ]
        for activity_name, description in activities:
            call_quietly(self.application.add_extracurricular, activity_name, description)

        self.assertEqual(len(self.extracurriculars()), 3)
        #Each activity gets its own ID, so no two of them collide
        ids = [item.extracurricular_id for item in self.extracurriculars()]
        self.assertEqual(ids, [1, 2, 3])
        output = str(self.application)
        for activity_name, _ in activities:
            self.assertIn(activity_name, output)

    '''Test multiple previous education records'''
    def test_multiple_prev_edus(self) -> None:
        records = [
            ("SFBU", "BSc Computer Science", 2024),
            ("City College", "Associate Degree", 2021),
            ("Lincoln High", "Diploma", 2018),
        ]
        for institution, degree, year_completed in records:
            call_quietly(self.application.add_prev_edu, institution, degree, year_completed)

        self.assertEqual(len(self.previous_educations()), 3)
        ids = [record.prev_edu_id for record in self.previous_educations()]
        self.assertEqual(ids, [1, 2, 3])
        output = str(self.application)
        for institution, _, _ in records:
            self.assertIn(institution, output)

    '''Test removing an extracurricular activity that is not there'''
    def test_remove_nonexistent_extracurricular(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        printed = call_quietly(self.application.remove_extracurricular, 99)

        #Nothing is removed and the application says so instead of raising
        self.assertEqual(len(self.extracurriculars()), 1)
        self.assertIn("We can't find any curricular with ID: 99", printed)

    def test_remove_extracurricular_from_an_empty_list(self) -> None:
        printed = call_quietly(self.application.remove_extracurricular, 1)
        self.assertEqual(self.extracurriculars(), [])
        self.assertIn("We can't find any curricular with ID: 1", printed)

    '''Test removing a previous education record that is not there'''
    def test_remove_nonexistent_prev_edu(self) -> None:
        call_quietly(self.application.add_prev_edu, "SFBU", "BSc", 2024)
        printed = call_quietly(self.application.remove_prev_edu, 99)

        self.assertEqual(len(self.previous_educations()), 1)
        self.assertIn("We can't find any previous education with ID: 99", printed)

    def test_remove_prev_edu_from_an_empty_list(self) -> None:
        printed = call_quietly(self.application.remove_prev_edu, 1)
        self.assertEqual(self.previous_educations(), [])
        self.assertIn("We can't find any previous education with ID: 1", printed)


class TestApplicationSystemSearch(unittest.TestCase):
    def setUp(self) -> None:
        Application.id_counter = 0
        Extracurricular.id_counter = 0
        PreviousEducation.id_counter = 0

        self.system = ApplicationSystem()

        self.ann = Application(
            "Ann Lee", "555-0100", "ann@example.com", "1 Main St", Program("Computer Science")
        )
        call_quietly(self.ann.add_prev_edu, "City College", "Associate Degree", 2021)

        self.bob = Application(
            "Bob Tran", "555-0199", "bob@example.com", "2 Oak Ave", Program("Data Science")
        )
        call_quietly(self.bob.add_prev_edu, "City College", "Associate Degree", 2020)
        call_quietly(self.bob.add_prev_edu, "SFBU", "BSc Computer Science", 2023)

        self.cara = Application(
            "Cara Diaz", "555-0123", "cara@example.com", "3 Pine Rd", Program("Data Science")
        )
        call_quietly(self.cara.add_prev_edu, "SFBU", "BSc Computer Science", 2023)

        for application in (self.ann, self.bob, self.cara):
            call_quietly(self.system.add, application)

    def search(self, **criteria) -> list:
        '''Run a search without letting it print to the console'''
        results = []
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            results = self.system.search(**criteria)
        return results

    '''Test searching by applicant name'''
    def test_search_by_applicant_name(self) -> None:
        self.assertEqual(self.search(applicant_name="Bob Tran"), [self.bob])

    '''Test searching by program applied for'''
    def test_search_by_program(self) -> None:
        #Two applicants applied for the same program, so both of them come back
        self.assertCountEqual(self.search(program_applied="Data Science"), [self.bob, self.cara])

    '''Test searching by previous education'''
    def test_search_by_previous_education_institution(self) -> None:
        self.assertCountEqual(self.search(prev_edu="City College"), [self.ann, self.bob])

    def test_search_matches_any_of_the_education_records(self) -> None:
        #Bob has two records, and the second one is enough to find him
        self.assertEqual(self.search(prev_edu="SFBU"), [self.bob, self.cara])

    '''Test that each criterion is optional'''
    def test_search_without_any_criterion_returns_everything(self) -> None:
        self.assertEqual(self.search(), [self.ann, self.bob, self.cara])

    def test_search_combines_the_criteria_that_were_given(self) -> None:
        #Bob and Cara both applied for Data Science and both studied at SFBU
        self.assertEqual(
            self.search(program_applied="Data Science", prev_edu="SFBU"), [self.bob, self.cara]
        )
        self.assertEqual(
            self.search(applicant_name="Cara Diaz", program_applied="Data Science"), [self.cara]
        )

    def test_search_with_all_three_criteria(self) -> None:
        self.assertEqual(
            self.search(
                applicant_name="Ann Lee",
                program_applied="Computer Science",
                prev_edu="City College",
            ),
            [self.ann],
        )

    '''Test the searches that find nothing'''
    def test_search_with_no_match(self) -> None:
        self.assertEqual(self.search(applicant_name="Nobody At All"), [])

    def test_search_criteria_that_match_different_applications(self) -> None:
        #Ann matches the name and Bob matches the program, but no single application matches both
        self.assertEqual(self.search(applicant_name="Ann Lee", program_applied="Data Science"), [])

    def test_search_is_an_exact_match(self) -> None:
        #A partial name or the wrong letter case does not match
        self.assertEqual(self.search(applicant_name="Ann"), [])
        self.assertEqual(self.search(applicant_name="ann lee"), [])

    def test_search_reports_how_many_it_found(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            self.system.search(program_applied="Data Science")
        self.assertIn("Found 2 application(s)", buffer.getvalue())


class TestProgramCatalogue(unittest.TestCase):
    def setUp(self) -> None:
        Application.id_counter = 0
        self.system = ApplicationSystem()

    def test_the_system_starts_with_no_program(self) -> None:
        self.assertEqual(self.system.program_list, [])

    def test_add_program_keeps_the_object_it_is_given(self) -> None:
        computer_science = Program("Computer Science")
        self.system.add_program(computer_science)
        #The system stores that very object, it does not build one of its own -> Aggregation
        self.assertIs(self.system.program_list[0], computer_science)

    def test_add_program_refuses_something_that_is_not_a_program(self) -> None:
        printed = call_quietly(self.system.add_program, "Computer Science")
        self.assertIn("Wrong type of object", printed)
        self.assertEqual(self.system.program_list, [])

    def test_several_applications_share_one_program_object(self) -> None:
        data_science = Program("Data Science")
        self.system.add_program(data_science)

        first = Application("Ann Lee", "1", "a@b.c", "1 Main St", data_science)
        second = Application("Bob Tran", "2", "b@b.c", "2 Oak Ave", data_science)

        #Both applications point at the same Program, so there is only one of it in the system
        self.assertIs(first.program_applied, second.program_applied)
        self.assertIs(first.program_applied, data_science)

    def test_choose_a_program_gives_back_the_one_that_is_picked(self) -> None:
        computer_science = Program("Computer Science")
        data_science = Program("Data Science")
        self.system.add_program(computer_science)
        self.system.add_program(data_science)

        with patch("builtins.input", side_effect=["2"]):
            with redirect_stdout(io.StringIO()):
                chosen = self.system.choose_a_program()
        self.assertIs(chosen, data_science)

    def test_choose_a_program_asks_again_after_a_choice_that_is_not_offered(self) -> None:
        computer_science = Program("Computer Science")
        self.system.add_program(computer_science)

        buffer = io.StringIO()
        #0, 5 and a word are all refused before 1 is accepted
        with patch("builtins.input", side_effect=["0", "5", "the first one", "1"]):
            with redirect_stdout(buffer):
                chosen = self.system.choose_a_program()
        self.assertIs(chosen, computer_science)
        self.assertEqual(buffer.getvalue().count("That is not one of the programs"), 3)

    def test_choose_a_program_when_nothing_is_offered(self) -> None:
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            chosen = self.system.choose_a_program()
        #Nothing is asked, so no answer is needed and None comes back
        self.assertIsNone(chosen)
        self.assertIn("There is no program offered at the moment", buffer.getvalue())


class TestApplicationSystemUpdate(unittest.TestCase):
    def setUp(self) -> None:
        Application.id_counter = 0
        Extracurricular.id_counter = 0
        PreviousEducation.id_counter = 0

        self.system = ApplicationSystem()
        #The programs the applications choose from, 1. Computer Science and 2. Data Science
        self.computer_science = Program("Computer Science")
        self.data_science = Program("Data Science")
        self.system.add_program(self.computer_science)
        self.system.add_program(self.data_science)

        self.application = Application(
            "Ann Lee", "555-0100", "ann@example.com", "1 Main St", self.computer_science
        )
        call_quietly(self.system.add, self.application)

    def update(self, application_id: int, *typed_answers: str) -> str:
        '''Run update() with the menu answers already typed in, and give back what it printed'''
        buffer = io.StringIO()
        with patch("builtins.input", side_effect=list(typed_answers)):
            with redirect_stdout(buffer):
                self.system.update(application_id)
        return buffer.getvalue()

    '''Test that an ID which is not in the system is handled'''
    def test_update_with_an_unknown_id(self) -> None:
        #No menu is shown at all, so no answer needs to be typed
        printed = self.update(99)
        self.assertIn("We can't find any application with ID: 99", printed)
        self.assertNotIn("What do you want to update?", printed)

    '''Test that the right application is found'''
    def test_update_finds_the_application_by_its_id(self) -> None:
        printed = self.update(1, "0")
        self.assertIn("Updating the application with ID: 1", printed)
        self.assertIn("Finished updating the application with ID: 1", printed)

    def test_update_picks_the_application_whose_id_matches(self) -> None:
        second = Application(
            "Bob Tran", "555-0199", "bob@example.com", "2 Oak Ave", self.data_science
        )
        call_quietly(self.system.add, second)

        #Changing application 2 to program 1 must leave application 1 alone
        self.update(2, "1", "1", "0")
        self.assertEqual(second.program_applied.program_name, "Computer Science")
        self.assertEqual(self.application.program_applied.program_name, "Computer Science")

    '''Test each menu choice, which is where the Application methods get used'''
    def test_update_changes_the_program(self) -> None:
        #Menu choice 1, then program 2 from the list the college offers
        self.update(1, "1", "2", "0")
        self.assertEqual(self.application.program_applied.program_name, "Data Science")

    def test_update_shares_the_program_object_instead_of_making_a_new_one(self) -> None:
        self.update(1, "1", "2", "0")
        #The application points at the very same Program the system offers -> Aggregation
        self.assertIs(self.application.program_applied, self.data_science)

    def test_update_refuses_a_program_that_is_not_offered(self) -> None:
        #Program 9 is not on the list, so it asks again and 2 is taken
        printed = self.update(1, "1", "9", "2", "0")
        self.assertIn("That is not one of the programs", printed)
        self.assertIs(self.application.program_applied, self.data_science)

    def test_update_changes_the_status(self) -> None:
        self.update(1, "2", "ACCEPTED", "0")
        self.assertEqual(self.application.status, ApplicationStatus.ACCEPTED)

    def test_update_accepts_a_status_in_any_letter_case(self) -> None:
        self.update(1, "2", "reviewed", "0")
        self.assertEqual(self.application.status, ApplicationStatus.REVIEWED)

    def test_update_refuses_a_status_that_does_not_exist(self) -> None:
        printed = self.update(1, "2", "APPROVED", "0")
        self.assertIn("APPROVED is not one of the statuses", printed)
        #The application keeps the status it already had
        self.assertEqual(self.application.status, ApplicationStatus.PENDING)

    def test_update_adds_an_extracurricular(self) -> None:
        self.update(1, "3", "Robotics Club", "Built a robot", "0")
        self.assertEqual(len(self.application.extracurricular_list), 1)
        self.assertIn("Robotics Club", str(self.application))

    def test_update_removes_an_extracurricular(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        self.update(1, "4", "1", "0")
        self.assertEqual(self.application.extracurricular_list, [])

    def test_update_reports_an_extracurricular_id_that_is_not_there(self) -> None:
        call_quietly(self.application.add_extracurricular, "Robotics Club", "Built a robot")
        printed = self.update(1, "4", "99", "0")
        self.assertIn("We can't find any curricular with ID: 99", printed)
        self.assertEqual(len(self.application.extracurricular_list), 1)

    def test_update_adds_a_previous_education(self) -> None:
        self.update(1, "5", "SFBU", "BSc Computer Science", "2024", "0")
        self.assertEqual(len(self.application.previous_education_list), 1)
        self.assertEqual(self.application.previous_education_list[0].year_completed, 2024)

    def test_update_removes_a_previous_education(self) -> None:
        call_quietly(self.application.add_prev_edu, "SFBU", "BSc", 2024)
        self.update(1, "6", "1", "0")
        self.assertEqual(self.application.previous_education_list, [])

    def test_update_shows_the_application(self) -> None:
        printed = self.update(1, "7", "0")
        self.assertIn("Application_id: 1", printed)
        self.assertIn("Full name: Ann Lee", printed)

    '''Test the answers that are not usable'''
    def test_update_refuses_a_year_that_is_not_a_number(self) -> None:
        printed = self.update(1, "5", "SFBU", "BSc", "last year", "0")
        self.assertIn("The year has to be a number", printed)
        self.assertEqual(self.application.previous_education_list, [])

    def test_update_asks_again_after_a_choice_that_is_not_on_the_menu(self) -> None:
        printed = self.update(1, "42", "0")
        self.assertIn("That is not one of the choices", printed)
        #The menu is printed twice, once before the bad answer and once after it
        self.assertEqual(printed.count("What do you want to update?"), 2)

    '''Test several changes made one after another in the same menu session'''
    def test_update_makes_several_changes_in_one_session(self) -> None:
        self.update(
            1,
            "1", "2",
            "2", "ACCEPTED",
            "3", "Chess Team", "Regional tournaments",
            "5", "City College", "Associate Degree", "2021",
            "0",
        )
        self.assertEqual(self.application.program_applied.program_name, "Data Science")
        self.assertEqual(self.application.status, ApplicationStatus.ACCEPTED)
        self.assertEqual(len(self.application.extracurricular_list), 1)
        self.assertEqual(len(self.application.previous_education_list), 1)


class TestApplicationSystemDelete(unittest.TestCase):
    def setUp(self) -> None:
        Application.id_counter = 0
        Extracurricular.id_counter = 0
        PreviousEducation.id_counter = 0

        self.system = ApplicationSystem()
        self.ann = Application(
            "Ann Lee", "555-0100", "ann@example.com", "1 Main St", Program("Computer Science")
        )
        self.bob = Application(
            "Bob Tran", "555-0199", "bob@example.com", "2 Oak Ave", Program("Data Science")
        )
        self.cara = Application(
            "Cara Diaz", "555-0123", "cara@example.com", "3 Pine Rd", Program("Data Science")
        )
        for application in (self.ann, self.bob, self.cara):
            call_quietly(self.system.add, application)

    #The list is private, so the tests read it through its name mangled attribute
    def applications(self) -> list:
        return self.system._ApplicationSystem__application_list

    '''Test that an existing application can be deleted by its ID'''
    def test_delete_an_existing_application(self) -> None:
        printed = call_quietly(self.system.delete, 2)
        self.assertIn("Successfully deleted the application with ID: 2", printed)

    '''Test that the deleted application is gone from the list'''
    def test_the_deleted_application_is_no_longer_in_the_list(self) -> None:
        call_quietly(self.system.delete, 2)
        self.assertNotIn(self.bob, self.applications())
        self.assertEqual(len(self.applications()), 2)
        self.assertNotIn("Bob Tran", str(self.system))

    '''Test that the other applications are left alone'''
    def test_the_other_applications_are_unchanged(self) -> None:
        call_quietly(self.system.delete, 2)
        #Deleting swaps with the last one before popping, so the two that are left can be in any order
        self.assertCountEqual(self.applications(), [self.ann, self.cara])
        self.assertCountEqual([item.application_id for item in self.applications()], [1, 3])
        #Their data is untouched
        self.assertEqual(self.ann.applicant.full_name, "Ann Lee")
        self.assertEqual(self.cara.program_applied.program_name, "Data Science")

    def test_delete_the_first_application(self) -> None:
        call_quietly(self.system.delete, 1)
        self.assertCountEqual(self.applications(), [self.bob, self.cara])

    def test_delete_the_last_application(self) -> None:
        call_quietly(self.system.delete, 3)
        self.assertCountEqual(self.applications(), [self.ann, self.bob])

    def test_delete_every_application_one_by_one(self) -> None:
        for application_id in (1, 2, 3):
            call_quietly(self.system.delete, application_id)
        self.assertEqual(self.applications(), [])

    '''Test that an ID which is not in the system is handled'''
    def test_delete_an_id_that_does_not_exist(self) -> None:
        printed = call_quietly(self.system.delete, 99)
        self.assertIn("We can't find any application with ID: 99", printed)
        #Nothing is deleted and nothing is raised
        self.assertEqual(len(self.applications()), 3)

    def test_delete_the_same_application_twice(self) -> None:
        call_quietly(self.system.delete, 2)
        printed = call_quietly(self.system.delete, 2)
        self.assertIn("We can't find any application with ID: 2", printed)
        self.assertEqual(len(self.applications()), 2)

    def test_delete_from_an_empty_system(self) -> None:
        empty_system = ApplicationSystem()
        printed = call_quietly(empty_system.delete, 1)
        self.assertIn("We can't find any application with ID: 1", printed)

    '''Test that a deleted application is really out of the system'''
    def test_a_deleted_application_is_not_found_by_search(self) -> None:
        call_quietly(self.system.delete, 2)
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            results = self.system.search(applicant_name="Bob Tran")
        self.assertEqual(results, [])

    def test_a_deleted_application_can_not_be_updated(self) -> None:
        call_quietly(self.system.delete, 2)
        printed = call_quietly(self.system.update, 2)
        self.assertIn("We can't find any application with ID: 2", printed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
