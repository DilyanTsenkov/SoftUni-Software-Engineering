import unittest
from project.train.train import Train


class TestTrain(unittest.TestCase):
    NAME = "test name"
    CAPACITY = 2

    def setUp(self):
        self.testing_train = Train(self.NAME, self.CAPACITY)

    def test_train_name__expect_to_be_str(self):
        self.assertTrue(isinstance(self.testing_train.name, str))

    def test_train_capacity__expect_to_be_int(self):
        self.assertTrue(isinstance(self.testing_train.capacity, int))

    def test_train_init__when_correct_input_expect_be_initialized(self):
        self.assertEqual(TestTrain.NAME, self.testing_train.name)
        self.assertEqual(TestTrain.CAPACITY, self.testing_train.capacity)
        self.assertEqual([], self.testing_train.passengers)

    def test_train_add__when_passengers_become_more_than_capacity__expect_value_error(self):
        self.testing_train.passengers = ["test1", "test2"]
        passenger_name = "test3"
        with self.assertRaises(ValueError) as context:
            self.testing_train.add(passenger_name)
        self.assertEqual("Train is full", str(context.exception))

    def test_train_add__when_try_to_add_existing_passenger_name__expect_value_error(self):
        self.testing_train.passengers.append("test1")
        passenger_name = "test1"
        with self.assertRaises(ValueError) as context:
            self.testing_train.add(passenger_name)
        self.assertEqual(f"Passenger {passenger_name} Exists", str(context.exception))

    def test_train_add__expect_to_append_passenger(self):
        passenger_name = "test1"
        self.testing_train.add(passenger_name)
        self.assertEqual(["test1"], self.testing_train.passengers)

    def test_train_add__expect_to_return_correct_answer(self):
        passenger_name = "test1"
        self.assertEqual(f"Added passenger {passenger_name}", self.testing_train.add(passenger_name))

    def test_train__when_try_to_remove_unexisting_passenger_name__expect_value_error(self):
        passenger_name = "test1"
        self.testing_train.add(passenger_name)
        with self.assertRaises(ValueError) as context:
            self.testing_train.remove("test2")
        self.assertEqual("Passenger Not Found", str(context.exception))

    def test_train_expect_to_remove_passenger(self):
        passenger_name = "test1"
        self.testing_train.add(passenger_name)
        self.testing_train.remove("test1")
        self.assertEqual([], self.testing_train.passengers)

    def test_train_remove__expect_to_return_correct_answer(self):
        passenger_name = "test1"
        self.testing_train.add(passenger_name)
        passenger_name = "test1"
        self.assertEqual(f"Removed {passenger_name}", self.testing_train.remove(passenger_name))


if __name__ == '__main__':
    unittest.main()
