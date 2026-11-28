from abc import ABC, abstractmethod
from person import Guide
class ExpeditionWindow:
    def __init__(self, season_name: str, start_date: str, end_date: str, activity_description: str, max_capacity: int, guide: Guide, expedition_id = ""):
        self.__id = "expedition" + str(id(self))
        self.__season_name = season_name
        self.__start_date = start_date
        self.__end_date = end_date
        self.__activity_description = activity_description
        self.__max_capacity = max_capacity
        self.__guide = guide
        if expedition_id != "":
            self.__id = expedition_id
    def assign_guide(self, guide: Guide) -> None:
        if isinstance(guide, Guide):
            self.__guide = guide
            print(f"Change Guide successfully\n New guide: {guide}")
        else:
            print(f"{guide} is not a guide")

    def to_row(self) -> tuple:
        window = (self.__id, self.__season_name, self.__start_date, self.__end_date, self.__activity_description, self.__max_capacity, self.__guide)
        return window

    @staticmethod
    def from_row(window):
        id, season_name, start_date, end_date, activity_description, max_capacity, guide = window
        return ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)

    @property
    def id(self):
        return self.__id

    @property
    def guide(self):
        return self.__guide

    # a plain window has no difficulty, the decorators add it
    def get_required_skills(self) -> dict[str, str]:
        return {}

    def get_difficulty_names(self) -> list[str]:
        return []

class ExpeditionDecorator(ExpeditionWindow, ABC):
    def __init__(self, window: ExpeditionWindow):
        # no super().__init__(): the decorator keeps no trip data, it passes calls to the wrapped window
        self.__window = window

    @property
    def id(self):
        return self.__window.id

    @property
    def guide(self):
        return self.__window.guide

    def assign_guide(self, guide: Guide) -> None:
        self.__window.assign_guide(guide)

    def to_row(self) -> tuple:
        return self.__window.to_row()

    def get_required_skills(self) -> dict[str, str]:
        return self.__window.get_required_skills()

    def get_difficulty_names(self) -> list[str]:
        names = self.__window.get_difficulty_names()
        names.append(self.get_difficulty_name())
        return names

    @abstractmethod
    def get_difficulty_name(self) -> str:
        pass

class GlacierTrip(ExpeditionDecorator):
    def get_required_skills(self) -> dict[str, str]:
        skills = super().get_required_skills()
        skills["crevasse rescue"] = "intermediate"
        return skills

    def get_difficulty_name(self) -> str:
        return "glacier"

class SummitTrip(ExpeditionDecorator):
    def get_required_skills(self) -> dict[str, str]:
        skills = super().get_required_skills()
        skills["ice climbing"] = "advanced"
        skills["rope rescue"] = "intermediate"
        return skills

    def get_difficulty_name(self) -> str:
        return "summit"

class ExpeditionFactory:
    def __init__(self):
        self.__decorator = {"glacier": GlacierTrip, "summit": SummitTrip}

    def create_trip(self, trip_type: str, window: ExpeditionWindow) -> ExpeditionWindow:
        new_window = window
        if trip_type in self.__decorator:
            new_window = self.__decorator[trip_type](window)
        else:
            print(f"{trip_type} is not a trip type")
        return new_window

    def create_trip_by_names(self, trip_types: list[str], window: ExpeditionWindow) -> ExpeditionWindow:
        '''wrap the window once per name, in the saved order (used when loading from the database)'''
        new_window = window
        for trip_type in trip_types:
            new_window = self.create_trip(trip_type, new_window)
        return new_window
