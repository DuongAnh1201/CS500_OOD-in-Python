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
    def __init__(self, obj: Database, ) -> None:
        self.__obj = obj

    def execute(self):
        sql = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)"
        self.__obj.dp_query(sql)
        print("Created table 'users'")

class InserTableCommand(Command):
    pass

class UpdateTableCommand(Command):
    pass

class RemoveTableCommand(Command):
    pass


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

    invoker.run_all()

if __name__ == "__main__":
    main()
