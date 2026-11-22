"""
Question 2 lab 14
"""
from abc import ABC, abstractmethod
class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class Database:
    def __init__(self) -> None:
        pass
    def insert(self):
        print("Inserting command")
    
    def update(self):
        print("Updating command")
    
    def delete(self):
        print("Deleting command")
    

class InsertCommand(Command):
    def __init__(self, obj: Database):
        self.__obj = obj
    def execute(self):
        self.__obj.insert()

class UpdateCommand(Command):
    def __init__(self, obj: Database):
        self.__obj = obj
    def execute(self):
        self.__obj.update()

class DeleteCommand(Command):
    def __init__(self, obj: Database):
        self.__obj = obj
    def execute(self):
        self.__obj.delete()

class Client:
    def __init__(self):
        self.__command = None

    def setCommand(self, command: Command):
        self.__command = command

    def executeCommand(self):
        if self.__command is None:
            print("Command is not set")
        else:
            self.__command.execute()

def main():
    db = Database()
    client = Client()

    client.setCommand(InsertCommand(db))
    client.executeCommand()   # Inserting command

    client.setCommand(UpdateCommand(db))
    client.executeCommand()   # Updating command

    client.setCommand(DeleteCommand(db))
    client.executeCommand()   # Deleting command

if __name__ == "__main__":
    main()
