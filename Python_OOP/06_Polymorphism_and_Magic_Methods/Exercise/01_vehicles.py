from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_CONSUMPTION = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def needed_fuel(self, distance):
        return distance * (self.fuel_consumption + Car.SUMMER_CONSUMPTION)

    def is_fuel_enough(self, distance):
        return self.needed_fuel(distance) <= self.fuel_quantity

    def drive(self, distance):
        if self.is_fuel_enough(distance):
            self.fuel_quantity -= self.needed_fuel(distance)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_CONSUMPTION = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def needed_fuel(self, distance):
        return distance * (self.fuel_consumption + Truck.SUMMER_CONSUMPTION)

    def is_fuel_enough(self, distance):
        return self.needed_fuel(distance) <= self.fuel_quantity

    def drive(self, distance):
        if self.is_fuel_enough(distance):
            self.fuel_quantity -= self.needed_fuel(distance)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)
truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
