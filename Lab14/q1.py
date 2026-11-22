#Commands
from abc import abstractmethod, ABC

class Light:
    def on(self):
        pass

    def off(self):
        pass

class Fan:
    def start(self):
        pass

    def stop(self):
        pass


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightOncommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj


    def execute(self) -> None:
        self.__obj.on()

class LightOffcommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj

    def execute(self):
        self.__obj.off()

#Create the other two command classes


#Invoker
class RemoteControl:
    def setCommand(self, command):
        if isinstance(command, LightOncommand):
            self.__lightOnCommand = command
        elif isinstance(command, LightOffcommand):
            self.__lightoffcommand = Command

    def lightOnButtonPressed(self) -> None:
        self.__lightOnCommand.execute()

    def lightOffButtonPressed(self) -> None:
        self.__lightoffcommand.execute()

def main():
    light = Light()
    fan = Fan()
    control = RemoteControl()
    control.setCommand(LightOncommand(light))
    control.setCommand(LightOffcommand(light))

    control.lightOnButtonPressed()
    control.lightOffButtonPressed()

if __name__ == "__main__":
    main() 