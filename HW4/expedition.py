from curses import window
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
            self.__guide = Guide
            print(f"Change Guide successfully\n New guide: {guide}")
        else:
            print(f"{guide} is not a guide")

    def to_row(self) -> tuple: 
        window = (self.__id, self.__season_name, self.__start_date, self.__end_date, self.__activity_description, self.__max_capacity, self.__guide)
        return window

    @staticmethod
    def from_row(self):
        id, season_name, start_date, end_date, activity_description, max_capacity, guide = window
        return ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)

    @property
    def id(self):
        return self.__id

    @property
    def guide(self):
        return self.__guide