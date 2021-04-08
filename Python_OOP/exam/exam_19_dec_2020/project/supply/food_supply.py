from project.supply.supply import Supply
from project.survivor import Survivor


class FoodSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=20)

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
