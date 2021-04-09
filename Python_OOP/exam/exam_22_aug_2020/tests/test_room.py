import unittest

from project.rooms.room import Room
from project.appliances.fridge import Fridge
from project.appliances.laptop import Laptop
from project.appliances.tv import TV
from project.people.child import Child

class TestRoom(unittest.TestCase):
    family_name = "test name"
    budget = 100.00
    members_count = 2

    def setUp(self):
        self.testing_room = Room(TestRoom.family_name, TestRoom.budget, TestRoom.members_count)

    def test_room_family_name__expect_to_be_str(self):
        self.assertTrue(isinstance(TestRoom.family_name, str))

    def test_room_budget__expect_to_be_int(self):
        self.assertTrue(isinstance(TestRoom.budget, float))

    def test_room_members_count_expect_to_be_int(self):
        self.assertTrue(isinstance(TestRoom.members_count, int))

    def test_room_init__when_correct_input_expect_be_initialized(self):
        self.assertEqual(TestRoom.family_name, self.testing_room.family_name)
        self.assertEqual(TestRoom.budget, self.testing_room.budget)
        self.assertEqual(TestRoom.members_count, self.testing_room.members_count)
        self.assertEqual([], self.testing_room.children)
        self.assertEqual(0,self.testing_room.expenses)

    def test_room_expenses__when_expenses_below_0__expect_exception(self):
        with self.assertRaises(ValueError) as context:
            self.testing_room.expenses = -1
        self.assertEqual("Expenses cannot be negative", str(context.exception))

    def test_room_calculate_expense__with_appliance(self):
        result = self.testing_room.calculate_expenses([TV(), Fridge(), Laptop()])
        self.assertEqual(111, result)

    def test_room_calculate_expense__with_children(self):
        child1 = Child(5, 1, 2, 1)
        child2 = Child(3, 2)
        result = self.testing_room.calculate_expenses([child1,child2])
        self.assertEqual(420, result)


if __name__ == '__main__':
    unittest.main()
