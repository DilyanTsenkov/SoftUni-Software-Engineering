class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        current_room = [r for r in self.rooms if room_number == r.number]
        if current_room:
            if people <= current_room[0].capacity and not current_room[0].is_taken:
                current_room[0].is_taken = True
                self.guests += people
                current_room[0].guests += people

    def free_room(self, room_number):
        current_room = [r for r in self.rooms if room_number == r.number]
        if current_room:
            current_room[0].is_taken = False
            self.guests -= current_room[0].guests
            current_room[0].guests = 0

    def print_status(self):
        free_rooms = [room for room in self.rooms if not room.is_taken]
        free_rooms_numbers = [str(room.number) for room in free_rooms]
        taken_rooms = [room for room in self.rooms if room.is_taken]
        taken_rooms_numbers = [str(room.number) for room in taken_rooms]
        print(f"Hotel {self.name} has {self.guests} total guests")
        if free_rooms_numbers:
            print(f"Free rooms: {', '.join(free_rooms_numbers)}")
        if taken_rooms_numbers:
            print(f"Taken rooms: {', '.join(taken_rooms_numbers)}")


class Room:
    def __init__(self, number, capacity):
        self.number = number
        self.capacity = capacity
        self.guests = 0
        self.is_taken = False

    @staticmethod
    def can_not_take_room(is_taken, capacity, people):
        return is_taken or capacity < people

    def take_room(self, people):
        if self.can_not_take_room(self.is_taken, self.capacity, people):
            return f"Room number {self.number} cannot be taken"
        self.is_taken = True
        self.guests += people

    def free_room(self):
        if not self.is_taken:
            return f"Room number {self.number} is not taken"
        self.is_taken = False
        self.guests = 0


hotel = Hotel.from_stars(5)

first_room = Room(1, 3)
second_room = Room(2, 2)
third_room = Room(3, 1)

hotel.add_room(first_room)
hotel.add_room(second_room)
hotel.add_room(third_room)

hotel.take_room(1, 4)
hotel.take_room(1, 2)
hotel.take_room(3, 1)
hotel.take_room(3, 1)

hotel.print_status()
