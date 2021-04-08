from project.medicine.medicine import Medicine
from project.survivor import Survivor


class Salve(Medicine):
    def __init__(self):
        super().__init__(health_increase=50)

    def apply(self, survivor: Survivor):
        survivor.health += self.health_increase
