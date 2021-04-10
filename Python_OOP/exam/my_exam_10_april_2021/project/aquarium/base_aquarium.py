from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    @abstractmethod
    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not value:
            raise ValueError("Aquarium name cannot be an empty string.")
        self._name = value

    def calculate_comfort(self):
        result = sum([dec.comfort for dec in self.decorations])
        return result

    def add_fish(self, fish):
        if len(self.fish) < self.capacity:
            self.fish.append(fish)
            return f"Successfully added {fish.__class__.__name__} to {self.name}."
        else:
            return "Not enough capacity."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = f"{self.name}:\n"
        if self.fish:
            fish_names = [fish.name for fish in self.fish]
            result += f"Fish: {' '.join(fish_names)}\n"
        else:
            result += f"Fish: none\n"
        result += f"Decorations: {len(self.decorations)}\n"
        result += f"Comfort: {self.calculate_comfort()}"
        return result

