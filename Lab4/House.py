class Room:
    def __init__(self, type: str, size: int):
        self.__type = type
        self.__size = size
    
    @property
    def size(self) -> int:
        return self.__size

    def __str__(self) -> str:
        return f"Type room: {self.__type}, size room: {self.__size}"

    def __repr__(self) -> str:
        return self.__str__()


class Garage:
    def __init__(self, type: str, size: int, door_type: str):
        self.__type = type
        self.__size = size
        self.__door_type = door_type

    @property
    def size(self) -> int:
        return self.__size
    
    @size.setter
    def size(self, new_size: int) -> None:
        self.__size = new_size

    def __str__(self) -> str:
        return f"Garage type: {self.__type}, garage size: {self.__size}, garage door type: {self.__door_type}"

    def __repr__(self) -> str:
        return self.__str__()

class Television:
    def __init__(self, screen_type: str, screen_size: int, resolution: str, price: float):
        self.__screen_type = screen_type
        self.__screen_size = screen_size
        self.__resolution = resolution
        self.__price = price

    @property
    def screen_type(self) -> str:
        return self.__screen_type
    
    @property
    def screen_size(self) -> int:
        return self.__screen_size

    @property
    def resolution(self) -> str:
        return self.__resolution
    
    @property
    def price(self) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'''TV Object:
                Screen type: {self.__screen_type}
                Screen size: {self.__screen_size}
                Resolution: {self.__resolution}
                Price: {self.__price}
        '''

    def __repr__(self) -> str:
        return self.__str__()
    
    def __eq__(self, value: object) -> bool:
        if isinstance(value, Television):
            return self.__screen_type == value.screen_type and self.__screen_size == value.screen_size and self.__resolution == value.resolution and self.__price == value.price
        return False

class House:
    def __init__(self, address: str, square_feet: int, rooms: list[Room], garage: Garage, televisions: list[Television]):
        self.__address = address
        self.__square_feet = square_feet
        self.__rooms = []
        for room in rooms:
            self.__rooms.append(room)
        self.__garage = garage 
        self.__televisions = []
        for television in televisions:
            self.__televisions.append(television)

    @property
    def square_feet(self) -> int:
        return self.__square_feet
    def change_garage_size(self, new_size: int) -> None:
        self.__garage.size = new_size
        print("Change the garage size successfully")

    def add_TV (self, television: Television) -> None:
        self.__televisions.append(television)
        print("Add one more TV successfully")

    def remove_TV(self, television: Television) -> None:
        ok = False
        for i in range(len(self.__televisions)):
            if self.__televisions[i].__eq__(television):
                self.__televisions[i] = self.__televisions[-1]
                self.__televisions.pop()
                ok = True
                print("Remove 1 TV successfully")
                break
        if ok == False:
            print("Can find the appropriate TV object")

    def get_biggest_room(self) -> Room | None:
        largest: Room | None = None
        for room in self.__rooms:
            if largest == None:
                largest = room
            if room.size > largest.size:
                largest = room
        return largest

    def get_oled_televisions(self) -> list[Television] | list[None]:
        oled_television =[]
        for television in self.__televisions:
            if television.screen_type == "OLED":
                oled_television.append(television)
        return oled_television

    def number_of_rooms(self) -> int:
        return len(self.__rooms)

    def __eq__(self, value):
        if isinstance(value, House):
            return self.__square_feet == value.square_feet and self.number_of_rooms() == value.number_of_rooms()
        return False
    def is_similar_house(self, other) -> bool:
        return self.__eq__(other)

    def __str__(self) -> str:
        return f''' House Object:
                Address: {self.__address}
                Square feet: {self.__square_feet}
                Rooms: {self.__rooms}
                Garage: {self.__garage}
                televisions: {self.__televisions}
        '''

    def __repr__(self) -> str:
        return self.__str__()
    

def main():
    garage = Garage("single", 1000, "auto")
    room_1 = Room("Bedroom", 1000)
    room_2 = Room("Bedroom", 1500)
    room_3 = Room("Bathroome", 500)
    room_4 = Room("Store room", 800)
    rooms = [room_1, room_2, room_3, room_4]

    tv_1 = Television("OLED", 100, "4K", 2000)
    tv_2 = Television("OLED", 70, "2K", 1000)
    tv_3 = Television("LCD", 50, "2K", 500)
    tv_4 = Television("LCD", 65, "4K", 800)

    televisions = [tv_1, tv_2, tv_3, tv_4]

    house_1 = House("161 Mission Falls Lane",
                    100000, 
                    rooms,
                    garage,
                    televisions)
    print(f"House 1 information {house_1}")
    tv_5 = Television("Retina", 100, "2K", 1000)
    house_1.add_TV(tv_5)
    print(f"After add one TV: {house_1}")
    house_1.change_garage_size(800)
    largest_room = house_1.get_biggest_room()
    print(f"Biggest room: {largest_room}")
    oled_tv = house_1.get_oled_televisions()
    print(oled_tv)

    garage_2 = Garage("double", 2000, "auto")
    house_2 = House("79 Wenatchee",
                    100000,
                    rooms,
                    garage_2,
                    televisions)

    print(f"House 2 information: {house_2}")
    print(f"House 1 is similar to House 2: {house_1.is_similar_house(house_2)}")

if __name__ == "__main__":
    main()