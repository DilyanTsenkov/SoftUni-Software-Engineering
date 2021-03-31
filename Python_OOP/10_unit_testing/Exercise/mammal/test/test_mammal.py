import unittest

from project.mammal import Mammal


class TestMammal(unittest.TestCase):
    expected_name = "Test Name"
    expected_type = "Test Type"
    expected_sound = "Test Sound"

    def setUp(self):
        self.test_mammal = Mammal("Test Name", "Test Type", "Test Sound")

    def test_mammal_init__when_correct_name_type_sound_expect_be_initialized(self):
        self.assertEqual(self.expected_name, self.test_mammal.name)
        self.assertEqual(self.expected_type, self.test_mammal.type)
        self.assertEqual(self.expected_sound, self.test_mammal.sound)

    def test_mammal_make_sound__expect_to_return_name_makes_sound(self):
        current = self.test_mammal.make_sound()
        expected = f"{self.expected_name} makes {self.expected_sound}"
        self.assertEqual(current, expected)

    def test_mammal_kingdom__expect_initial(self):
        current = self.test_mammal._Mammal__kingdom
        expected_kingdom = "animals"
        self.assertEqual(current, expected_kingdom)

    def test_mammal_get_kingdom__expect_to_return_kingdom(self):
        current = self.test_mammal.get_kingdom()
        expected_kingdom = "animals"
        self.assertEqual(current, expected_kingdom)

    def test_mammal_info__expect_to_return_name_is_of_type_type(self):
        expected = f"{self.expected_name} is of type {self.expected_type}"
        current = self.test_mammal.info()
        self.assertEqual(current, expected)


if __name__ == '__main__':
    unittest.main()
