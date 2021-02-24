class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = int(health)

    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []

    def add_pokemon(self, pokemon):
        if pokemon in self.pokemon:
            return f"This pokemon is already caught"
        self.pokemon.append(pokemon)
        return f"Caught {pokemon.name} with health {pokemon.health}"

    def release_pokemon(self, pokemon_name):
        pokemon_finder = [p for p in self.pokemon if p.name == pokemon_name]
        if pokemon_finder:
            self.pokemon.remove(pokemon_finder[0])
            return f"You have released {pokemon_name}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        data = f"Pokemon Trainer {self.name}\nPokemon count {len(self.pokemon)}\n"
        for el in self.pokemon:
            data += f"- {el.name} with health {el.health}\n"
        return data

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
