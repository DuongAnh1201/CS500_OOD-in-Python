class Product:
    def __init__(self, product_id: int, product_name: str, price: float)-> None:
        self.__product_id = product_id
        self.__product_name = product_name
        self.__price = price

    @property
    def product_id(self):
        return self.__product_id

    @property
    def price(self) -> float:
        return self.__price

    @price.getter
    def price(self, price: float) -> None:
        self.__price = price

    def __str__(self) ->str:
        return f"product_ID: {self.__product_id}, product_name: {self.__product_name}, price: {self.__price}"

    def __repr__(self) ->str:
        return self.__str__(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Product):
            return self.__product_id == value.__product_id
        return False
class Customer:
    def __init__(self, name: str, address: str) -> None:
        self.__name = name
        self.__address = address

    @property
    def name(self)->str:
        return self.__name
    
    @property
    def address(self) -> str:
        return self.__address
    @address.setter
    def address(self, address) -> None:
        self.__address = address

    def __str__(self)-> str:
        return f"Customer name: {self.__name}, Customer address: {self.__address}"
    
    def __repr__(self) -> str:
        return self.__str__(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, Customer):
            return self.__name == value.__name and self.__address == value.__address
        return False

class OrderItem:
    def __init__(self,  product: Product, quantity: int):
        self.__product = product       #Aggregation
        self.__quantity = quantity

    @property
    def product(self) -> Product:
        return self.__product
    @property
    def quantity(self) -> int:
        return self.__quantity

    @quantity.setter
    def quantity(self, quantity) -> None:
        self.__quantity = quantity

    def get_total_value(self) -> float:
        return self.__product.price * self.__quantity
    def __str__(self) -> str:
        return f"Order Product: {self.__product}, quantity: {self.__quantity}"

    def __repr__(self) -> str:
        return self.__str__(self)

    def __eq__(self, value: object) -> bool:
        if isinstance(value, OrderItem):
            return self.__product == value.__product
        return False

class Order:
    def __init__(self, orderid: int, customer: Customer) -> None:
        self.__orderid = orderid
        self.__customer = customer #Aggregation
        self.__order_items: list[OrderItem] = []
    
    def add_item(self, product: Product, quantity: int) -> None:

        for item in self.__order_items:
            if product.__eq__(item):  
                item.quantity += quantity
                return
        self.__order_items.append(OrderItem(product, quantity)) #Composition
    
    def remove_item(self, product_id: int) -> None:
        for ind in range(len(self.__order_items)):
            if self.__order_items[ind].product.product_id == product_id:
                self.__order_items[ind] = self.__order_items[-1]
                self.__order_items.pop()
    
    def find_largest_item(self) -> OrderItem | None:
        largest: OrderItem | None = None
        total = 0
        for item in self.__order_items:
            if largest == None:
                largest = item
                total = item.get_total_value()
            else:
                total_item = item.get_total_value()
                if total<total_item:
                    largest = item
                    total = total_item
        return largest
        
            



def main():
    p1 = Product(111, "Hammer", 20.99)
    p2 = Product(222, "Saw", 30.99)
    p3 = Product(333, "Nail", 0.99)
    # products = [p1, p2, p3]

    customer = Customer("Peter", "123 Mission Blvd, Fremont")
    order = Order(123, customer)
    order.add_item(p1, 100)
    order.add_item(p2, 10)
    order.add_item(p3, 20)

    


if __name__ == "__main__":
    main()