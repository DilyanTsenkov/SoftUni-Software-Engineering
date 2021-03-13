from project.animals.animal import Bird
from project.food import *


class Owl(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.25
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)
        self.food_eaten = 0

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * 0.35
        self.food_eaten += food.quantity
