from HW4.expedition import ExpeditionWindow
from interface import Repository
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
    def save(self, gear_type):
        gear_id = gear_type + str(id(gear_type))
        gear_row = (gear_id)
        obj = self.__factory.create_gear_by_id(gear_type, gear_id)
        sql = f"""INSERT INTO  inventory (ID, gear_type, condition_ratings, maintenance_records, is_avail)
        VALUES (?,?,?,?,?)
        """
        row_id, gear_type, condition_ratings, maintenance_records, is_avail = obj.to_row()
        # sqlite cannot store a list, so save the records as text
        self.__db.db_query(sql, (row_id, gear_type, condition_ratings, str(maintenance_records), is_avail))
        print("Save new gear successfully")

    def find_by_id(self, obj_id) -> Gear|None:
        sql = f"""SELECT * from inventory WHERE ID = ?"""
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        row_id, gear_type, condition_ratings, maintenance_records, is_avail = obj
        gear = self.__factory.create_gear_by_tuple(gear_type, obj)
        return gear[0]
    def find_all(self) -> None:
        sql = f"""SELECT * from inventory"""
        gears = self.__db.db_query(sql, params = [])
        for gear in gears:
            print(gear)

    def update(self, obj_id) -> None:
        obj = self.find_by_id(obj_id)
        if not obj:
            return None
        fix_data = input("Which part do you want to update (condition_ratings, maintenance_records, status)")
        value = input("Value = ")
        sql = f"""UPDATE inventory
                    SET {fix_data} = ?
                    WHERE ID = ?
                    """
        if fix_data == "condition_ratings":
            value = float(value)
        self.__db.db_query(sql, (value,))
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
        customers = self.__db.db_query(sql, params=[])
        for customer in customers:
            print(customer)

    def update(self, obj_id: str)-> None:
        obj = self.find_by_id(obj_id)
        if not obj:
            return None
        fix_data = input("Which part do you want to update (first_name, last_name, age, phone, email)")
        value = input("Value = ")
        sql = f"""UPDATE customer
                    SET {fix_data} = ?
                    WHERE ID = ?
                    """
        if fix_data == "age":
            value = int(value)
        self.__db.db_query(sql, (value, obj_id))
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

    def find_all(self) -> None:
        sql = """SELECT ID FROM guide"""
        guide_ids = self.__db.db_query(sql, params=[])
        for guide_id in guide_ids:
            guide = self.find_by_id(guide_id[0])
            print(guide)
            print()

    def update(self, obj_id) -> None:
        sql = """ """
        obj = self.find_by_id(obj_id)
        if not obj:
            return None
        fix_data = input("Which part do you want to update (first_name, last_name, age, phone, certified, daily_avail, technical_skills)")
        # skills live in their own table: add a new skill or change its level
        if fix_data == "technical_skills":
            skill = input("Skill = ")
            level = input("Level = ")
            sql = """INSERT OR REPLACE INTO guide_skills (guide_id, skill, level)
                    VALUES (?, ?, ?)"""
            self.__db.db_query(sql, (obj_id, skill, level))
            print("Update value successfully")
            return None
        value = input("Value = ")
        sql = f"""UPDATE guide
                    SET {fix_data} = ?
                    WHERE ID = ?
                    """
        if fix_data == "age":
            value = int(value)
        if fix_data == "certified":
            value = value == "True"
        # daily_avail is typed as dates separated by commas, e.g. 2026-12-01,2026-12-02
        self.__db.db_query(sql, (value, obj_id))
        print("Update value successfully")

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
        self.__columns = {"ID": "TEXT PRIMARY KEY", "season_name": "TEXT", "start_date": "TEXT", "end_date": "TEXT", "activity_description": "TEXT", "max_capacity": "INTEGER", "guide": "TEXT"}
        self.__db.create_tables("expedition", self.__columns)

    def save(self, obj: ExpeditionWindow) -> None:
        id, season_name, start_date, end_date, activity_description, max_capacity, guide = obj.to_row()
        guide_id = obj.guide.id
        sql = """
        INSERT INTO expedition (ID, season_name, start_date, end_date, activity_description, max_capacity, guide)
        VALEUS (?, ?, ?, ?, ?, ?, ?)
        """
        self.__db.db_query(sql, (id, season_name, start_date, end_date, activity_description, max_capacity, guide))
        print("Add new expedition reservation successfully!")

    def find_by_id(self, obj_id) -> ExpeditionWindow|None:
        sql = """
        SELECT * FROM expedition 
        WHERE ID = ?
        """
        obj = self.__db.db_query(sql, (obj_id, ))
        if len(obj) == 0:
            return None
        id, season_name, start_date, end_date, activity_description, max_capacity, guide_id = obj[0]
        guide = self.__db_guide.find_by_id(guide_id)
        expedition_window = ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)
        return expedition_window

    def find_all(self) -> list:
        sql = """
        SELECT * from expedition
        """
        expedition_windows = []
        expedition_data = self.__db.db_query(sql, params= [])
        for expedition in expedition_data:
            id, season_name, start_date, end_date, activity_description, max_capacity, guide_id = expedition
            guide = self.__db_guide.find_by_id(guide_id)
            expedition_window = ExpeditionWindow(season_name, start_date, end_date, activity_description, max_capacity, guide, id)
            expedition_windows.append(expedition_window)
        return expedition_windows

    def update(self, obj_id) -> None:
        obj = self.find_by_id(obj_id)
        if not obj:
            return None
        fix_data = input("Which part do you want to update (season_name, start_date, end_date, activity_description, max_capacity, guide)")
        sql = f"""
        UPDATE expedition
        SET {fix_data} = ?
        WHERE ID = ?
        """
        value = input("Value: ")
        if fix_data == 'max_capacity':
            value = int(value)
            self.__db.db_query(sql, (value, obj_id))
            print("Update successfully!")
            return None
    
        self.__db.db_query(sql, (value, obj_id))
        print("Update successfully")
        return None
        

class GearRequestRepository(Repository):
    pass
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
        self.__db.db_query(sql, (id, customer_id, expedition_reservation_id, gear_request_ids, created_at, status))
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
        expedition_reservation = self.__db__expedition.find_by_id(expedition_reservation_id) 
        gear_requests = []
        gear_request_ids = gear_request_ids.split(",")
        for gear_request_id in gear_request_ids:
            gear_request: GearRequest = self.__db_gear_request.find_by_id(gear_request_id)
            gear_requests.append(gear_request)
        return Reservation(customer, expedition_reservation, gear_requests, created_at, status, id)
    
    def find_all(self) -> list:
        sql = """
        SELECT * from reservation
        """
        reservations = []
        reservation_data = self.__db.db_query(sql, params = [])
        for reservation in reservation_data:
            id, customer_id, expedition_reservation_id, gear_request_ids, created_at, status = reservation
            customer = self.__db_customer.find_by_id(customer_id)
            expedition_reservation = self.__db__expedition.find_by_id(expedition_reservation_id) 
            gear_requests = []
            gear_request_ids = gear_request_ids.split(",")
            for gear_request_id in gear_request_ids:
                gear_request: GearRequest = self.__db_gear_request.find_by_id(gear_request_id)
                gear_requests.append(gear_request)
            reservations.append(Reservation(customer, expedition_reservation, gear_request, created_at, status, id))
        return reservations

    def update(self, obj_id) -> None:
        obj = self.find_by_id(obj_id)
        if not obj:
            return None
        fix_data = input("Which part do you want to update (customer_id, expedition_reservation_id, gear_request_id, created_at, status)")
        sql = f"""
            UPDATE reservation
            SET {fix_data} = ?
            WHERE ID = ?        
        """
        self.__db.db_query(sql, (fix_data, obj_id))
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

    # # save dummy gears
    # repo.save("rope")
    # repo.save("tent")
    # repo.save("beacon")

    # # show all gears
    # repo.find_all()

    # # find one gear by a dummy ID
    # gear = repo.find_by_id("rope001")
    # print(gear)

    # # update a dummy gear (asks for the field and value)
    # repo.update("rope001")

    # # delete a dummy gear
    # repo.delete("rope001")
    # repo.find_all()

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
    guide_repo.find_all()

    # find one guide by ID
    guide = guide_repo.find_by_id(minh.id)
    print(guide)

    # update a guide (asks for the field and value)
    guide_repo.update(minh.id)

    # delete a guide
    guide_repo.delete(lan.id)
    guide_repo.find_all()

if __name__ == "__main__":
    main()
