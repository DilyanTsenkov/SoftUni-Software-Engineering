from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, side, height):
        self.side = side
        self.height = height

    def calculate_area(self):
        return self.side * self.height / 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return self.radius * self.radius * pi


class AreaCalculator:
    def __init__(self, shapes):
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.calculate_area()
        return total

    @property
    def shape(self):
        return self.__shapes

    @shape.setter
    def shape(self, value):
        if not isinstance(value, list):
            raise TypeError("`shapes` should be of type `list`.")
        res = [shape for shape in value if not isinstance(shape, Shape)]
        if res:
            raise TypeError("All `shapes` should be of type `Shape`.")
        self.__shapes = value


shapes = [Rectangle(1, 6), Triangle(2, 3), Circle(3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)
