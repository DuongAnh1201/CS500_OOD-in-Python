from abc import ABC, abstractmethod
import sqlite3
#Receiver
class Database:
    def __init__(self, db_file: str) -> None:
        self.__conn = sqlite3.connect(db_file)

    def dp_query(self, query, params = []) -> list[any]:
        cursor = self.__conn.cursor()
        cursor.execute(query, params)
        self.__conn.commit()
        return cursor.fetchall()

#Command
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class CreateTableCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        self.__obj.dp_query(sql)
        print("Created table 'users'")

class InserTableCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        sql = """INSERT INTO users (id, name, age)
        VALUES (1, 'Duong Anh Nguyen', 20),
        (2, 'Peter', 50);"""
        self.__obj.dp_query(sql)
        print("Inserting into table 'users'")

class ReadTableCommand(Command): 
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        sql = """
        SELECT * from users;
        """
        self.__obj.dp_query(sql)
        print("Reading the whole table")

class UpdateTableCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        sql = """
        UPDATE users
        SET age = 25
        WHERE id = 1;
        """
        self.__obj.dp_query(sql)
        print("Update table")
        
class RemoveTableCommand(Command):
    def __init__(self, obj: Database) -> None:
        self.__obj = obj

    def execute(self) -> None:
        sql = """
        DELETE users
        WHERE id = 2;
        """
        self.__obj.dp_query(sql)
        print("Remove record")

    


#Invoker
class DatabaseInvoker:
    def __init__(self) -> None:
        self.__commands: list[Command] = []
        
    def set_command(self, command: Command):
        self.__commands.append(command)



    def run_all(self):
        for command in self.__commands:
            command.execute()


#main
def main():
    db: Database = Database("Testdb.db")
    invoker: DatabaseInvoker = DatabaseInvoker()
    invoker.set_command(CreateTableCommand(db))
    invoker.set_command(InserTableCommand(db))
    invoker.set_command(ReadTableCommand(db))
    invoker.run_all()

if __name__ == "__main__":
    main()
