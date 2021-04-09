from project.rooms.room import Room


class AloneOld(Room):
    members_count = 1

    def __init__(self, family_name: str, pension: float):
        super().__init__(family_name, pension, self.members_count)
        self.room_cost = 10
