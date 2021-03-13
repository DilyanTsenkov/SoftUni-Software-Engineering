from project.animals.animal import Mammal
from project.food import Vegetable, Fruit, Meat


class Mouse(Mammal):
    WEIGHT_INCREASE_CONS = 0.1

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Fruit):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Mouse.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity


class Dog(Mammal):
    WEIGHT_INCREASE_CONS = 0.40

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Dog.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity


class Cat(Mammal):
    WEIGHT_INCREASE_CONS = 0.30

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if not isinstance(food, Vegetable) and not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Cat.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity


class Tiger(Mammal):
    WEIGHT_INCREASE_CONS = 1.00

    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Tiger.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity
