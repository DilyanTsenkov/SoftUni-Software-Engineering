from project.animals.animal import Bird
from project.food import Meat


class Owl(Bird):
    WEIGHT_INCREASE_CONS = 0.25

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if not isinstance(food, Meat):
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity * Owl.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity


class Hen(Bird):
    WEIGHT_INCREASE_CONS = 0.35

    def __init__(self, name, weight, wing_size):
        super().__init__(name, weight, wing_size)

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * Hen.WEIGHT_INCREASE_CONS
        self.food_eaten += food.quantity
