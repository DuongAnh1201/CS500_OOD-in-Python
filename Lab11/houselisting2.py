from abc import ABC, abstractmethod

class Displayable(ABC):
    @abstractmethod
    def display(self):
        pass


class House(Displayable):
    def __init__(self, address:str, square_feet:int, num_rooms:int, price:float, city: str):
        self.__address = address
        self.__square_feet = square_feet
        self.__num_rooms = num_rooms
        self.__price = price
        self.__city = city

    # add some public properties here if necessary 
    @property
    def address(self) -> str:
        return self.__address

    @property
    def price(self) -> float:
        return self.__price
    @price.setter
    def price(self, new_price: float) -> None:
        self.__price = new_price
    def __str__(self) -> str:
        return f"Address = {self.__address}, Square Feet = {self.__square_feet}, Number of Rooms = {self.__num_rooms}, Price = {self.__price}"

    def display(self) -> None:
        print(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, House):
            return self.__address == value.__address
        return False


class Contact(Displayable):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str) -> None:
        self.__lastname = lastname
        self.__firstname = firstname
        self.__email = email
        self.__phone_number = phone_number

    # add some public properties here if necessary 

    def __str__(self) -> str:
        return f"Last Name = {self.__lastname}, First Name = {self.__firstname}, Phone Number = {self.__phone_number}, Email = {self.__email}"

    def display(self):
        print(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Contact):
            return self.__email == value.__email
        return False

class Owner(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str):
        super().__init__(firstname, lastname, phone_number, email)
        self.__houses = []

    def add_house(self, house):
        self.__houses.append(house)

    def __str__(self):
        output = super().__str__()
        output += "\nOwns the following houses: "
        for house in self.__houses:
            output+= f"\n{house}"

        return output

class Buyer(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str):
        super().__init__(firstname, lastname, phone_number, email)
        self.__watch_list = []

    @property
    def watch_list(self):
        return self.__watch_list

    # Return the index of the house in the watch list, or -1 if not found
    def search_house(self, house: House) -> int:
        for i in range(len(self.__watch_list)):
            if self.__watch_list[i] == house:
                return i
        return -1

    #  Save the house in his watch list
    def save_to_watchlist(self, house: House) -> None:
        if self.search_house(house) != -1:
            print("Already in watchlist")
        else:
            self.__watch_list.append(house)

    # Remove the house from his watch list
    def remove_from_watchlist(self, house: House) -> None:
        index = self.search_house(house)
        if index != -1:
            self.__watch_list.pop(index)
        else:
            print("House not in watchlist")

    def __str__(self)-> str:
        output = super().__str__() + "\nWatching the following house: "
        for house in self.__watch_list:
            output += f"\n{house}"
        return output


class Company(Displayable):
    def __init__(self, companyName):
        self.__companyName = companyName
        self.__owners: list[Owner] = []
        self.__buyers: list[Buyer] = []
        self.__agents: list[Agent] = []
        self.__houses: list[House] = []

    def add_owner(self, owner: Owner):
        if owner not in self.__owners:
            self.__owners.append(owner)

    def add_buyer(self, buyer: Buyer):
        if buyer not in self.__buyers:
            self.__buyers.append(buyer)

    def add_agent(self, agent):
        if agent not in self.__agents:
            self.__agents.append(agent)

    def add_house_to_listing(self, house: House):
        if house not in self.__houses:
            self.__houses.append(house)

    def get_house_by_address(self, address: str) -> House|None:
        for house in self.__houses:
            if house.address == address:
                return house
        return None

    def remove_house_from_listing(self, house: House):
        for i in range(len(self.__houses)):
            if self.__houses[i] == house:
                self.__houses[i], self.__houses[-1] = self.__houses[-1], self.__houses[i]
                self.__houses.pop()
                break


    # Help to remove that house from all buyers' watch list.
    def remove_house_from_watchlist(self, house: House):
        for buyer in self.__buyers:
            buyer.remove_from_watchlist(house)

    # Return all buyers who have this house in their watch list
    def get_buyers_by_house(self, house: House) -> list:
        buyers = []
        for buyer in self.__buyers:
            if buyer.search_house(house) != -1:
                buyers.append(buyer)
        return buyers

    def __str__(self):
        output = f"Company Name = {self.__companyName}\n"

        output += "=========================== The list of agents: =============================="
        for agent in self.__agents:
            output += f"\n{agent}"

        output += "\n=========================== The house listing: ==============================="
        for house in self.__houses:
            output += f"\n{house}"

        output += "\n=========================== The list of owners: =============================="
        for owner in self.__owners:
            output += f"\n{owner}"

        output += "\n=========================== The list of buyers: =============================="
        for buyer in self.__buyers:
            output += f"\n{buyer}"

        return output
    def display(self):
        print(self)


class Agent(Contact):
    def __init__(self, firstname: str, lastname: str, phone_number: str, email: str, position: str, company: Company):
        super().__init__(firstname, lastname, phone_number, email)
        self.__position = position
        self.__company = company

    def add_house_to_listing_for_owner(self, owner: Owner, house: House):
        self.__company.add_owner(owner)
        self.__company.add_house_to_listing(house)

    def help_buyer_to_save_to_watchlist(self, buyer: Buyer, house: House):
        self.__company.add_buyer(buyer)
        buyer.save_to_watchlist(house)

    def edit_house_price(self, address: str, new_price: float):
        house = self.__company.get_house_by_address(address)
        if house:
            house.price = new_price

    def sold_house(self, house):
        self.__company.remove_house_from_listing(house)
        self.__company.remove_house_from_watchlist(house)
    # print all potential buyers who are interested in buying that house
    def display_potental_buyers(self, house):
        buyers = self.__company.get_buyers_by_house(house)

        for buyer in buyers:
            buyer.display()

    def __str__(self) -> str:
        output = super().__str__()
        output += f"\nPosition = {self.__position}"
        return output
    def display(self):
        print(self)

def main():
    owner1 = Owner('Peter', 'Li', '510-111-2222', 'peter@yahoo.com')
    owner2 = Owner('Carl', 'Buck', '408-111-2222', 'carl@yahoo.com')

    house1 = House('1111 Mission Blvd', 1000, 2, 1000000, 'Fremomt')
    house2 = House('2222 Mission Blvd', 2000, 3, 1500000, 'San Jose')
    house3 = House('3333 Mission Blvd', 3000, 4, 2000000, 'Mountain View')

    owner1.add_house(house1)
    owner2.add_house(house2)
    owner2.add_house(house3)

    buyer1 = Buyer('Tom', 'Buke', '408-555-2222', 'tom@yahoo.com')
    buyer2 = Buyer('Lily', 'Go', '510-222-3333', 'lily@yahoo.com')

    company = Company('Good Future Real Estate')
    agent1 = Agent('Dave', 'Henderson', '408-777-3333',
                   'dave@yahoo.com', 'Senior Agent', company)
    company.add_agent(agent1)

    agent1.add_house_to_listing_for_owner(owner1, house1)
    agent1.add_house_to_listing_for_owner(owner2, house2)
    agent1.add_house_to_listing_for_owner(owner2, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer1, house1)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer1, house3)

    agent1.help_buyer_to_save_to_watchlist(buyer2, house2)
    agent1.help_buyer_to_save_to_watchlist(buyer2, house3)

    agent1.edit_house_price('2222 Mission Blvd', 1200000)

    company.display()

    print('\nAfter one house was sold ..........................')
    agent1.sold_house(house3)
    company.display()

    print('\nDisplaying potential buyers for house 1 ..........................')
    agent1.display_potental_buyers(house1)



if __name__ == "__main__":
    main()
