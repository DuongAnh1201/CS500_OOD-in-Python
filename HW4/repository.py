from interface import Repository
from database import Database
from gears import Gear, InventoryFactory
from person import Customer, Guide, Person
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
        self.__db = Database("custome.db")
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

if __name__ == "__main__":
    main()
