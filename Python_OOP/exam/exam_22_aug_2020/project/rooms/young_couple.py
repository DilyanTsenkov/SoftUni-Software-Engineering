from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV


class YoungCouple(Room):
    room_members = 2
    room_cost = 20
    appliance_types = (TV, Fridge, Laptop)

    def __init__(self, family_name: str, salary_one: float, salary_two: float):
        super().__init__(family_name, salary_one + salary_two, self.room_members)
        self.calculate_expenses(self.appliances)
