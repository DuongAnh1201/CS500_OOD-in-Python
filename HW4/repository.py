from expedition import ExpeditionWindow, ExpeditionFactory
from interface import Repository, GearRequestStatus, ReservationStatus
from database import Database
from gears import Gear, GearRequest, InventoryFactory
from person import Customer, Guide, Person
from reservation import Reservation
class InventoryRepository(Repository):
    def __init__(self):
        self.__db = Database("inventory.db")
        self.__factory = InventoryFactory()
        self.__columns = {"ID": "TEXT PRIMARY KEY", "gear_type": "TEXT","condition_ratings": "REAL", "maintenance_records": "TEXT", "is_avail": "BOOLEAN"}
        self.__db.create_tables("inventory", self.__columns)
    def save(self, obj: Gear) -> None:
        sql = f"""INSERT INTO  inventory (ID, gear_type, condition_ratings, maintenance_records, is_avail)
        VALUES (?,?,?,?,?)
        """
        row_id, gear_type, condition_ratings, maintenance_records, is_avail = obj.to_row()
        self.__db.db_query(sql, (row_id, gear_type, condition_ratings, maintenance_records, is_avail))
        print("Save new gear successfully")

    def find_by_id(self, obj_id) -> Gear|None:
        sql = f"""SELECT * from inventory WHERE ID = ?"""
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        row_id, gear_type, condition_ratings, maintenance_records, is_avail = obj[0]
        gear = self.__factory.create_gear_by_tuple(gear_type, obj[0])
        return gear
    def find_all(self) -> list:
        sql = f"""SELECT * from inventory"""
        gear_datas = self.__db.db_query(sql, params = [])
        gears = []
        for gear_data in gear_datas:
            row_id, gear_type, condition_ratings, maintenance_records, is_avail = gear_data
            gears.append(self.__factory.create_gear_by_tuple(gear_type, gear_data))
        return gears
    def update(self, obj: Gear) -> None:
        id, gear_type, condition_ratings, maintenance_records, is_avail = obj.to_row()
        sql = f"""UPDATE inventory
                    SET gear_type = ?, condition_ratings = ?, maintenance_records = ?, is_avail = ?
                    WHERE ID = ?
                    """
        self.__db.db_query(sql, (gear_type, condition_ratings, maintenance_records, is_avail, id))
        print("Update value successfully")
    
    def delete(self, obj_id) -> None:
        sql = f"""DELETE from inventory
        WHERE ID = ? """
        self.__db.db_query(sql, (obj_id, ))

class CustomerRepository(Repository):
    def __init__(self) -> None:
        self.__db = Database("customer.db")
        self.__columns = {"ID": "TEXT PRIMARY KEY", "first_name": "TEXT", "last_name": "TEXT", "age": "INTEGER", "phone": "TEXT", "email": "TEXT"}
        self.__db.create_tables("customer", self.__columns)

    def save(self, obj: Customer) -> None:
        id, first_name, last_name, age,phone, email = obj.to_row()
        sql = """INSERT INTO customer (ID, first_name, last_name, age, phone, email)
                VALUES (?, ?, ?, ?, ?, ?) """
        self.__db.db_query(sql, (id, first_name, last_name, age, phone, email))
        print("Add new customer successfully!")

    def find_by_id(self, obj_id: str) -> Customer|None:
        sql = """ SELECT * FROM customer WHERE ID = ?
        """
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        customer = Customer.from_row(obj[0])
        return customer
    
    def find_all(self) -> None:
        sql = """SELECT * FROM customer"""
        customer_datas = self.__db.db_query(sql, params=[])
        customers = []
        for customer in customer_datas:
            customers.append(Customer.from_row(customer))
        return customers

    def update(self, obj: Customer)-> None:
        id, first_name, last_name, age, phone, email = obj.to_row()
        sql = f"""UPDATE customer
                    SET first_name = ?, last_name = ?, age = ?, phone = ?, email = ?
                    WHERE ID = ?
                    """
        self.__db.db_query(sql, (first_name, last_name, age, phone, email, id))
        print("Update value successfully")

    def delete(self, obj_id) -> None:
        sql = f"""DELETE from customer
        WHERE ID = ? """
        self.__db.db_query(sql, (obj_id, ))
        
class GuideRepository(Repository):
    def __init__(self):
        self.__db = Database("guide.db")
        self.__columns_guide = {"ID": "TEXT PRIMARY KEY", "first_name": "TEXT", "last_name": "TEXT", "age": "INTEGER", "phone": "TEXT", "certified":"BOOLEAN", "daily_avail": "TEXT"}
        self.__columns_guide_skills = {"guide_id": "TEXT", "skill": "TEXT", "level": "TEXT", "PRIMARY KEY": "(guide_id, skill)"
}
        self.__db.create_tables("guide", self.__columns_guide)
        self.__db.create_tables("guide_skills", self.__columns_guide_skills)

    def save(self, obj: Guide):
        id, first_name, last_name, age, phone, certified, technical_skills, daily_avail = obj.to_row()
        sql_guide = """ 
        INSERT INTO guide
        VALUES (?, ?, ?, ?, ?, ? , ?)
        """
        daily_avail = Guide.convert_list(daily_avail)
        self.__db.db_query(sql_guide, (id, first_name, last_name, age, phone, certified, daily_avail))

        sql_guide_skills = """
        INSERT INTO guide_skills
        VALUES (?, ?, ?)
        """
        for skill, level in technical_skills.items():
            self.__db.db_query(sql_guide_skills, (id, skill, level))
        print("Save successfully!")

    def find_by_id(self, obj_id):
        sql_guide = """ SELECT * FROM guide WHERE ID = ?
        """
        obj = self.__db.db_query(sql_guide, (obj_id, ))
        sql_guide_skill = """SELECT * FROM guide_skills WHERE guide_id = ?"""
        guide_id = self.__db.db_query(sql_guide_skill, (obj_id, ))
        if len(obj) == 0:
            return None
        id, first_name, last_name, age, phone, certified, daily_avail = obj[0]
        # rebuild the skills dict from the guide_skills rows
        technical_skills = {}
        for skill_row in guide_id:
            skill_guide_id, skill, level = skill_row
            technical_skills[skill] = level
        row = (id, first_name, last_name, age, phone, certified, technical_skills, Guide.convert_string(daily_avail))
        customer = Guide.from_row(row)
        return customer

    def find_all(self) -> list:
        sql = """SELECT ID FROM guide"""
        guide_ids = self.__db.db_query(sql, params=[])
        guides = []
        for guide_id in guide_ids:
            guide = self.find_by_id(guide_id[0])
            guides.append(guide)
        return guides

    def update(self, obj: Guide) -> None:
        id, first_name, last_name, age, phone, certified, technical_skills, daily_avail = obj.to_row()
        self.delete(id)
        self.save(obj)
        
        
        

    def delete(self, obj_id) -> None:
        # delete the skills first, then the guide
        sql_guide_skills = """DELETE from guide_skills
        WHERE guide_id = ? """
        self.__db.db_query(sql_guide_skills, (obj_id, ))
        sql_guide = """DELETE from guide
        WHERE ID = ? """
        self.__db.db_query(sql_guide, (obj_id, ))
        print("Delete successfully!")

class ExpeditionReservationRepository(Repository):
    def __init__(self) -> None:
        self.__db = Database("expedition.db")
        self.__db_guide = GuideRepository()
        self.__factory = ExpeditionFactory()
        self.__columns = {"ID": "TEXT PRIMARY KEY", "season_name": "TEXT", "start_date": "TEXT", "end_date": "TEXT", "activity_description": "TEXT", "max_capacity": "INTEGER", "guide": "TEXT", "difficulty": "TEXT"}
        self.__db.create_tables("expedition", self.__columns)

    def save(self, obj: ExpeditionWindow) -> None:
        id, season_name, start_date, end_date, activity_description, max_capacity, guide = obj.to_row()
        guide_id = obj.guide.id
        sql = """
        INSERT INTO expedition (ID, season_name, start_date, end_date, activity_description, max_capacity, guide, difficulty)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        difficulties = obj.get_difficulty_names()
        difficulty = ",".join(difficulties)
        self.__db.db_query(sql, (id, season_name, start_date, end_date, activity_description, max_capacity, guide_id, difficulty))
        print("Add new expedition reservation successfully!")

    def find_by_id(self, obj_id) -> ExpeditionWindow|None:
        sql = """
        SELECT * FROM expedition 
        WHERE ID = ?
        """
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        id, season_name, start_date, end_date, activity_description, max_capacity, guide_id, difficulty = obj[0]
        guide = self.__db_guide.find_by_id(guide_id)
        expedition_window = ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)
        return self.__add_difficulty(expedition_window, difficulty)

    def __add_difficulty(self, window: ExpeditionWindow, difficulty: str) -> ExpeditionWindow:
        if difficulty == "":
            return window
        return self.__factory.create_trip_by_names(difficulty.split(","), window)

    def find_all(self) -> list:
        sql = """
        SELECT * from expedition
        """
        expedition_windows = []
        expedition_data = self.__db.db_query(sql, params= [])
        for expedition in expedition_data:
            id, season_name, start_date, end_date, activity_description, max_capacity, guide_id, difficulty = expedition
            guide = self.__db_guide.find_by_id(guide_id)
            expedition_window = ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)
            expedition_windows.append(self.__add_difficulty(expedition_window, difficulty))
        return expedition_windows

    def update(self, obj: ExpeditionWindow) -> None:
        id, season_name, start_date, end_date, activity_description, max_capacity, guide = obj.to_row()
        difficulty = obj.get_difficulty_names()
        
        sql = f"""
        UPDATE expedition
        SET season_name = ?, start_date = ?, end_date = ?, activity_description = ?, max_capacity = ?, guide = ?, difficulty = ?
        WHERE ID = ?
        """
        
        self.__db.db_query(sql, (season_name, start_date, end_date, activity_description, max_capacity, guide.id, ",".join(difficulty), id))
        print("Update successfully")
        return None
        
    def delete(self, obj_id) -> None:
        sql = f"""
        DELETE FROM expedition
        WHERE ID = ?
        """
        self.__db.db_query(sql, (obj_id, ))
        print("Delete successfully")

    

class GearRequestRepository(Repository):
    def __init__(self):
        self.__db = Database("gear_request.db")
        self.__columns = {"ID": "TEXT", "gear_type": "TEXT", "quantity": "INTEGER", "notes": "TEXT", "status":"TEXT"}

        self.__db.create_tables("gear_request", self.__columns)

    def save(self, obj: GearRequest):
        sql = """
        INSERT INTO gear_request (ID, gear_type, quantity, notes, status)
        VALUES (?, ?, ?, ?, ?)
        """

        id, gear_type, quantity, notes, status = obj.to_row()
        self.__db.db_query(sql, (id, gear_type, quantity, notes, status.value))
        print("Save successfully!")

    def find_by_id(self, obj_id) -> GearRequest|None:
        sql = """
        SELECT * from gear_request
        WHERE ID = ?
        """
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        id, gear_type, quantity, notes, status = obj[0]
        return GearRequest(gear_type, quantity, notes, GearRequestStatus(status), id)

    def find_all(self) -> list:
        sql = """
        SELECT * from gear_request
        """
        gear_request_data = self.__db.db_query(sql, params = [])
        gear_requests = []
        for gear_request in gear_request_data:
            id, gear_type, quantity, notes, status = gear_request
            
            gear_requests.append(GearRequest(gear_type, quantity, notes, GearRequestStatus(status), id))

        return gear_requests

    def update(self, obj):
        id, gear_type, quantity, notes, status = obj.to_row()
        sql = f"""
        UPDATE gear_request
        SET gear_type = ?, quantity = ?, notes = ?, status = ?
        WHERE ID = ?
        """
        self.__db.db_query(sql, (gear_type, quantity, notes, status.value, id))
        print("Update successfully!")
        return None

    def delete(self, obj_id)-> None:
        sql = f"""
        DELETE from gear_request
        WHERE ID = ?
        """
        self.__db.db_query(sql, (obj_id, ))
        print("Delete successfully!")
        return None
            
class ReservationRepository(Repository):
    def __init__(self):
        self.__db = Database("reservation.db")
        self.__columns_reservation = {"ID": "TEXT", "customer": "TEXT", "expedition_reservation": "TEXT","gear_requests": "TEXT", "created_at": "TEXT", "status": "TEXT"}
        self.__db.create_tables("reservation", self.__columns_reservation)
        self.__db_customer = CustomerRepository()
        self.__db_expedition = ExpeditionReservationRepository()
        self.__db_gear_request = GearRequestRepository()

    def save(self, obj: Reservation):
        id, customer, expedition_reservation, gear_requests, created_at, status = obj.to_row()
        customer_id = customer.id
        expedition_reservation_id = expedition_reservation.id
        gear_request_ids = []
        for gear_request in gear_requests:
            gear_request_ids.append(gear_request.id)
        sql = """
        INSERT INTO reservation (ID, customer, expedition_reservation, gear_requests, created_at, status)
        VALUES (?, ?, ?, ?, ?, ?)
        """
        self.__db.db_query(sql, (id, customer_id, expedition_reservation_id, ",".join(gear_request_ids), created_at, status.value))
        print("Saved successfully")

    def find_by_id(self, obj_id):
        sql = """
        SELECT * from reservation
        WHERE ID = ?
        """
        obj = self.__db.db_query(sql, (obj_id,))
        if len(obj) == 0:
            return None
        id, customer_id, expedition_reservation_id, gear_request_ids, created_at, status = obj[0]
        customer = self.__db_customer.find_by_id(customer_id)
        expedition_reservation = self.__db_expedition.find_by_id(expedition_reservation_id) 
        gear_requests = []
        if gear_request_ids != "":
            for gear_request_id in gear_request_ids.split(","):
                gear_request: GearRequest = self.__db_gear_request.find_by_id(gear_request_id)
                gear_requests.append(gear_request)
        return Reservation(customer, expedition_reservation, gear_requests, created_at, ReservationStatus(status), id)
    
    def find_all(self) -> list:
        sql = """
        SELECT * from reservation
        """
        reservations = []
        reservation_data = self.__db.db_query(sql, params = [])
        for reservation in reservation_data:
            id, customer_id, expedition_reservation_id, gear_request_ids, created_at, status = reservation
            customer = self.__db_customer.find_by_id(customer_id)
            expedition_reservation = self.__db_expedition.find_by_id(expedition_reservation_id) 
            gear_requests = []
            if gear_request_ids != "":
                for gear_request_id in gear_request_ids.split(","):
                    gear_request: GearRequest = self.__db_gear_request.find_by_id(gear_request_id)
                    gear_requests.append(gear_request)
            reservations.append(Reservation(customer, expedition_reservation, gear_requests, created_at, ReservationStatus(status), id))
        return reservations

    def update(self, obj:Reservation) -> None:
        id, customer, expedition_reservation, gear_requests, created_at, status = obj.to_row()
        sql = f"""
            UPDATE reservation 
            SET customer = ?, expedition_reservation = ?, gear_requests = ?, created_at = ?, status = ? 
            WHERE ID = ?
        """ 
        gear_requests_id = []
        if len(gear_requests) != 0:
            for gear_request in gear_requests:
                gear_requests_id.append(gear_request.id)
        gear_requests_id = ",".join(gear_requests_id)
        self.__db.db_query(sql, (customer.id, expedition_reservation.id, gear_requests_id, created_at, status.value, id))
        print("Update value successfully")
        return None


    def delete(self, obj_id) -> None:
        sql = """
        DELETE FROM reservation
        WHERE ID = ?
        """
        self.__db.db_query(sql, (obj_id, ))
        print("Delete successfully!")
def main():
    repo = InventoryRepository()

    # save dummy gears (the factory creates them, main keeps them)
    factory = InventoryFactory()
    rope = factory.create_gear_by_id("rope")
    rope2 = factory.create_gear_by_id("rope")
    tent = factory.create_gear_by_id("tent")
    repo.save(rope)
    repo.save(rope2)
    repo.save(tent)

    # show all gears
    for gear in repo.find_all():
        print(gear.to_row())

    # find one gear by ID
    gear = repo.find_by_id(rope.to_row()[0])
    if gear:
        print(gear.to_row())

    # update a gear (asks for the field and value)
    repo.update(rope.to_row()[0])

    # delete a gear
    repo.delete(rope2.to_row()[0])
    for gear in repo.find_all():
        print(gear.to_row())

    customer_repo = CustomerRepository()

    # save dummy customers
    anna = Customer("Anna", "Tran", 25, "408-111-2222", "anna@example.com")
    ben = Customer("Ben", "Le", 31, "408-333-4444", "ben@example.com")
    customer_repo.save(anna)
    customer_repo.save(ben)

    # show all customers
    customer_repo.find_all()

    # find one customer by ID (ID is generated by Person)
    customer = customer_repo.find_by_id(anna.id)
    print(customer)

    # update a customer (asks for the field and value)
    customer_repo.update(anna.id)

    # delete a customer
    customer_repo.delete(ben.id)
    customer_repo.find_all()

    guide_repo = GuideRepository()

    # save dummy guides ("" lets Person generate the ID)
    minh = Guide("", "Minh", "Pham", 30, "408-555-6666", True, {"ice climbing": "advanced", "rope rescue": "intermediate"}, ["2026-12-01", "2026-12-02"])
    lan = Guide("", "Lan", "Vo", 27, "408-777-8888", False, {"navigation": "beginner"}, ["2026-12-05"])
    guide_repo.save(minh)
    guide_repo.save(lan)

    # show all guides
    for guide in guide_repo.find_all():
        print(guide)
        print()

    # find one guide by ID
    guide = guide_repo.find_by_id(minh.id)
    print(guide)

    # update a guide (asks for the field and value)
    guide_repo.update(minh.id)

    # delete a guide
    guide_repo.delete(lan.id)
    for guide in guide_repo.find_all():
        print(guide)
        print()

    expedition_repo = ExpeditionReservationRepository()

    # save dummy expeditions (minh is already saved in the guide repo)
    winter = ExpeditionWindow("Winter 2026", "2026-12-01", "2026-12-10", "Glacier trek", 8, minh)
    spring = ExpeditionWindow("Spring 2027", "2027-03-15", "2027-03-20", "Ice climbing course", 5, minh)
    expedition_repo.save(winter)
    expedition_repo.save(spring)

    # show all expeditions
    for expedition in expedition_repo.find_all():
        print(expedition.to_row())

    # find one expedition by ID
    expedition = expedition_repo.find_by_id(winter.id)
    if expedition:
        print(expedition.to_row())

    # update an expedition (asks for the field and value)
    expedition_repo.update(winter.id)

    gear_request_repo = GearRequestRepository()

    # save dummy gear requests
    rope_request = GearRequest("rope", 2, "60m dynamic rope", GearRequestStatus.PENDING)
    tent_request = GearRequest("tent", 1, "4-season tent", GearRequestStatus.PENDING)
    gear_request_repo.save(rope_request)
    gear_request_repo.save(tent_request)

    # show all gear requests
    for gear_request in gear_request_repo.find_all():
        print(gear_request)
        print()

    # find one gear request by ID
    gear_request = gear_request_repo.find_by_id(rope_request.id)
    print(gear_request)

    # update a gear request (asks for the field and value)
    gear_request_repo.update(rope_request.id)

    reservation_repo = ReservationRepository()

    # save dummy reservations (anna, winter and the gear requests are already saved)
    anna_reservation = Reservation(anna, winter, [rope_request, tent_request], "2026-11-27", ReservationStatus.PENDING)
    reservation_repo.save(anna_reservation)

    # show all reservations
    for reservation in reservation_repo.find_all():
        print(reservation.to_row())

    # find one reservation by ID
    reservation = reservation_repo.find_by_id(anna_reservation.id)
    if reservation:
        print(reservation.to_row())

    # update a reservation (asks for the field and value)
    reservation_repo.update(anna_reservation.id)

    # delete everything created by these tests
    reservation_repo.delete(anna_reservation.id)
    gear_request_repo.delete(tent_request.id)
    reservation_repo.find_all()
    gear_request_repo.find_all()

if __name__ == "__main__":
    main()
