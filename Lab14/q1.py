#Commands
from abc import abstractmethod, ABC
from calendar import c

class Light:
    def on(self):
        print("Light is turning on")

    def off(self):
        print("Light is turning off")

class Fan:
    def start(self):
        print("Fan is starting")

    def stop(self):
        print("Fan is stopping")


class Command(ABC):
    @abstractmethod
    def execute(self):
        pass

class LightOnCommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj


    def execute(self) -> None:
        self.__obj.on()

class LightOffCommand(Command):
    def __init__(self, obj: Light) -> None:
        self.__obj = obj

    def execute(self):
        self.__obj.off()

#Create the other two command classes
class FanStartCommand(Command):
    def __init__(self, obj: Fan) -> None:
        self.__obj = obj
    def execute(self):
        self.__obj.start()

class FanStopCommand(Command):
    def __init__(self, obj: Fan) -> None:
        self.__obj = obj
    def execute(self):
        self.__obj.stop()


#Invoker
class RemoteControl:
    def setCommand(self, command):
        if isinstance(command, LightOnCommand):
            self.__lightoncommand = command
        elif isinstance(command, LightOffCommand):
            self.__lightoffcommand = command
        elif isinstance(command, FanStartCommand):
            self.__fanstartcommand = command
        elif isinstance(command, FanStopCommand):
            self.__fanstopcommand = command
        else:
            print("Command is not in the list")

    def lightOnButtonPressed(self) -> None:
        self.__lightoncommand.execute()

    def lightOffButtonPressed(self) -> None:
        self.__lightoffcommand.execute()

    def fanStartButtonPressed(self) -> None:
        self.__fanstartcommand.execute()

    def fanStopButtonePressed(self) -> None:
        self.__fanstopcommand.execute()

def main():
    light = Light()
    fan = Fan()
    control = RemoteControl()
    control.setCommand(LightOnCommand(light))
    control.setCommand(LightOffCommand(light))
    control.setCommand(FanStartCommand(fan))
    control.setCommand(FanStopCommand(fan))
    control.lightOnButtonPressed()
    control.lightOffButtonPressed()
    control.fanStartButtonPressed()
    control.fanStopButtonePressed()

if __name__ == "__main__":
    main() 