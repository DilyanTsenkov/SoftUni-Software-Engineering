from project.fish.base_fish import BaseFish


class SaltwaterFish(BaseFish):
    SIZE = 5

    def __init__(self, name: str, species: str, price: float):
        super().__init__(name, species, self.SIZE, price)

    def eat(self):
        self.size += 2
        return self.size

