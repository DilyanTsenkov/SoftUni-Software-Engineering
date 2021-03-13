from project.animals.animal import Mammal
from project.food import *


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) or not isinstance(food, Fruit):
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.40
        self.food_eaten += food.quantity


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) or not isinstance(food, Meat):
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * 0.30
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.food_eaten = 0

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity
        self.food_eaten += food.quantity
