import math

#Target Interface (for RectangleAdapter) / Adaptee (for ShapeAdapter)
class ModernShape:
    def __init__(self, area: float, perimeter: float) -> None:
        self.__area = area
        self.__perimeter = perimeter

    def get_area(self) -> float:
        return self.__area

    def get_perimeter(self) -> float:
        return self.__perimeter

#Adaptee (for RectangleAdapter) / Target Interface (for ShapeAdapter)
class LegacyRectangle:
    def __init__(self, width: float, height: float) -> None:
        self.__width = width
        self.__height = height

    def get_width(self) -> float:
        return self.__width

    def get_height(self) -> float:
        return self.__height

#Adapter: LegacyRectangle -> ModernShape
#Adaptee here is LegacyRectangle
class RectangleAdapter(ModernShape):
    def __init__(self, obj: LegacyRectangle) -> None:
        self.__obj = obj

    def get_area(self) -> float:
        width = self.__obj.get_width()
        height = self.__obj.get_height()
        return width*height

    def get_perimeter(self) -> float:
        width = self.__obj.get_width()
        height = self.__obj.get_height()
        return (width+height)*2

#Adapter: ModernShape -> LegacyRectangle
#Adaptee here is ModernShape
#width + height = perimeter/2 and width * height = area
#=> width, height are the 2 roots of x^2 - (perimeter/2)x + area = 0
class ShapeAdapter(LegacyRectangle):
    def __init__(self, obj: ModernShape) -> None:
        self.__obj = obj

    def __get_sides(self) -> tuple:
        half = self.__obj.get_perimeter()/2
        area = self.__obj.get_area()
        delta = half*half - 4*area
        if delta < 0:
            raise ValueError("Area and perimeter do not form a rectangle")
        root = math.sqrt(delta)
        return (half+root)/2, (half-root)/2

    def get_width(self) -> float:
        return self.__get_sides()[0]

    def get_height(self) -> float:
        return self.__get_sides()[1]

class ShapeFactory:
    @staticmethod
    def create_shape(width: float, height: float) -> ModernShape:
        obj = LegacyRectangle(width, height)
        return RectangleAdapter(obj)

    @staticmethod
    def create_rectangle(area: float, perimeter: float) -> LegacyRectangle:
        obj = ModernShape(area, perimeter)
        return ShapeAdapter(obj)

def main():
    shape = ShapeFactory.create_shape(10, 20)
    print("Area: ", shape.get_area())
    print("Perimeter: ", shape.get_perimeter())

    rectangle = ShapeFactory.create_rectangle(200, 60)
    print("Width: ", rectangle.get_width())
    print("Height: ", rectangle.get_height())

if __name__ == "__main__":
    main()
