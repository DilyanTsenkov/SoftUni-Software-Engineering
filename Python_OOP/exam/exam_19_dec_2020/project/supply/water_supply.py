from project.supply.supply import Supply
from project.survivor import Survivor


class WaterSupply(Supply):
    def __init__(self):
        super().__init__(needs_increase=40)

    def apply(self, survivor: Survivor):
        survivor.needs += self.needs_increase
