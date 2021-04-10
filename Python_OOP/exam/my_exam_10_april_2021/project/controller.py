from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository: DecorationRepository = DecorationRepository()
        self.aquariums = []

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        if aquarium_type == "FreshwaterAquarium":
            aquarium = FreshwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        elif aquarium_type == "SaltwaterAquarium":
            aquarium = SaltwaterAquarium(aquarium_name)
            self.aquariums.append(aquarium)
            return f"Successfully added {aquarium_type}."
        else:
            return "Invalid aquarium type."

    def add_decoration(self, decoration_type: str):
        if decoration_type == "Ornament":
            decoration_object = Ornament()
            self.decorations_repository.add(decoration_object)
            return f"Successfully added {decoration_type}."
        elif decoration_type == "Plant":
            decoration_object = Plant()
            self.decorations_repository.add(decoration_object)
            return f"Successfully added {decoration_type}."
        else:
            return "Invalid decoration type."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):
        result_aquarium_name = [a for a in self.aquariums if a.name == aquarium_name]
        result_decoration_type = [d for d in self.decorations_repository.decorations if
                                  d.__class__.__name__ == decoration_type]
        if result_decoration_type and result_aquarium_name:
            result_aquarium_name[0].add_decoration(result_decoration_type[0])
            self.decorations_repository.decorations.remove(result_decoration_type[0])
            return f"Successfully added {decoration_type} to {aquarium_name}."
        else:
            return f"There isn't a decoration of type {decoration_type}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        result_aquarium_name = [a for a in self.aquariums if a.name == aquarium_name]
        if result_aquarium_name[0].capacity <= len(result_aquarium_name[0].fish):
            return "Not enough capacity."
        if fish_type == "FreshwaterFish":
            if isinstance(result_aquarium_name[0], FreshwaterAquarium):
                fish = FreshwaterFish(fish_name, fish_species, price)
                result_aquarium_name[0].add_fish(fish)
                return f"Successfully added {fish_type} to {aquarium_name}."
            else:
                return "Water not suitable."

        elif fish_type == "SaltwaterFish":
            if isinstance(result_aquarium_name[0], SaltwaterAquarium):
                fish = SaltwaterFish(fish_name, fish_species, price)
                result_aquarium_name[0].add_fish(fish)
            else:
                return "Water not suitable."
        else:
            return f"There isn't a fish of type {fish_type}."

    def feed_fish(self, aquarium_name: str):
        result_aquarium_name = [a for a in self.aquariums if a.name == aquarium_name]
        result_aquarium_name[0].feed()
        fed_count = len(result_aquarium_name[0].fish)
        return f"Fish fed: {fed_count}"

    def calculate_value(self, aquarium_name: str):
        result_aquarium_name = [a for a in self.aquariums if a.name == aquarium_name]
        fish_price = sum([f.price for f in result_aquarium_name[0].fish])
        decoration_price = sum([d.price for d in result_aquarium_name[0].decorations])
        return f"The value of Aquarium {aquarium_name} is {(fish_price + decoration_price):.2f}."

    def report(self):
        result = [a.__str__() for a in self.aquariums]
        return "\n".join(result)
