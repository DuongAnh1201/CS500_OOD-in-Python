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
        sql = """INSERT OR IGNORE INTO users (id, name, age)
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
        rows = self.__obj.dp_query(sql)
        print("Reading the whole table")
        for row in rows:
            print(row)

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
        DELETE FROM users
        WHERE id = 2;
        """
        self.__obj.dp_query(sql)
        print("Remove record")

    


#Invoker
class DatabaseInvoker:
    def __init__(self) -> None:
        self.__commands: dict[str, Command] = {}

    def set_command(self, command: Command):
        if isinstance(command, CreateTableCommand):
            self.__commands["create"] = command
        elif isinstance(command, InserTableCommand):
            self.__commands["insert"] = command
        elif isinstance(command, ReadTableCommand):
            self.__commands["read"] = command
        elif isinstance(command, UpdateTableCommand):
            self.__commands["update"] = command
        elif isinstance(command, RemoveTableCommand):
            self.__commands["remove"] = command
        else:
            print("Command is not in the list")

    def run(self, name: str):
        if name in self.__commands:
            self.__commands[name].execute()
        else:
            print(f"Command '{name}' is not set")

    def run_all(self):
        for command in self.__commands.values():
            command.execute()


#main
def main():
    db: Database = Database("Testdb.db")
    invoker: DatabaseInvoker = DatabaseInvoker()
    invoker.set_command(CreateTableCommand(db))
    invoker.set_command(InserTableCommand(db))
    invoker.set_command(ReadTableCommand(db))
    invoker.set_command(UpdateTableCommand(db))
    invoker.set_command(RemoveTableCommand(db))

    invoker.run("create")
    invoker.run("insert")
    invoker.run("read")
    invoker.run("update")
    invoker.run("read")

    #Or run all operations in order
    #invoker.run_all()

if __name__ == "__main__":
    main()

"""
How the pattern separates the UI from the database:
The Invoker (UI side) only calls execute() on Command objects. Each Command
holds one request, and the Database (receiver) only knows how to run queries.
The UI never talks to the database directly, so either side can change
without affecting the other.

Why adding a new operation is easy:
A new operation is just a new Command class. The Database and the existing
commands stay unchanged, and run()/run_all() work for it automatically.
"""