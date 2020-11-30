class Zoo:

    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fish)}\n"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}\n"
        result += f"Total animals: {animals}"
        return result


zoo_name = input()
zoo = Zoo(zoo_name)

animals = int(input())

for animal in range(animals):
    animal_species, animal_type = input().split(" ")
    zoo.add_animal(animal_species, animal_type)

species_to_print = input()

print(zoo.get_info(species_to_print))
