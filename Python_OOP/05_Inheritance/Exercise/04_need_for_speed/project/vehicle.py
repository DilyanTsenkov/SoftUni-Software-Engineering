class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel_consumption = self.__class__.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers):
        trip_consumption = float(kilometers * self.fuel_consumption)
        if self.fuel >= trip_consumption:
            self.fuel -= trip_consumption
