from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.stove import Stove
from project.appliances.tv import TV


class OldCouple(Room):
    room_members = 2
    room_cost = 15
    appliance_types = (TV, Fridge, Stove)

    def __init__(self, family_name: str, pension_one: float, pension_two: float):
        super().__init__(family_name, pension_one + pension_two, self.room_members)
        self.calculate_expenses(self.appliances)
