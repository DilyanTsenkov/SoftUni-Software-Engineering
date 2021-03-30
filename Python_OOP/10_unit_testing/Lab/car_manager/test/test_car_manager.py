import unittest

# from car_manager.car_manager import Car


class TestCar(unittest.TestCase):
    make = "Brand"
    model = "Model"
    fuel_consumption = 5
    fuel_capacity = 50

    def setUp(self):
        self.testing_car = Car(self.make, self.model, self.fuel_consumption, self.fuel_capacity)

    def test_car_init__when_correct_input_expect_be_initialized(self):
        make = "Brand"
        model = "Model"
        fuel_consumption = 5
        fuel_capacity = 50
        current_car = Car(make, model, fuel_consumption, fuel_capacity)
        self.assertEqual(current_car.make, self.testing_car.make)
        self.assertEqual(current_car.model, self.testing_car.model)
        self.assertEqual(current_car.fuel_consumption, self.testing_car.fuel_consumption)
        self.assertEqual(current_car.fuel_capacity, self.testing_car.fuel_capacity)

    def test_car_make__expect_to_return_make(self):
        make = "correct"
        self.testing_car.make = "correct"
        self.assertEqual(make, self.testing_car.make)

    def test_car_make_setter__when_none__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.make = None
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_make_setter__when_0__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.make = 0
        self.assertEqual("Make cannot be null or empty!", str(context.exception))

    def test_car_model__expect_to_return_model(self):
        model = "correct"
        self.testing_car.model = "correct"
        self.assertEqual(model, self.testing_car.model)

    def test_car_model_setter__when_none__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.model = None
        self.assertEqual("Model cannot be null or empty!", str(context.exception))

    def test_car_fuel_consumption__expect_to_return_fuel_consumption(self):
        fuel_consumption = 10
        self.testing_car.fuel_consumption = 10
        self.assertEqual(fuel_consumption, self.testing_car.fuel_consumption)

    def test_car_fuel_consumption_setter__when_equal_to_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_consumption_setter__when_smaller_than_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.fuel_consumption = -1
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity__expect_to_return_fuel_capacity(self):
        fuel_capacity = 100
        self.testing_car.fuel_capacity = 100
        self.assertEqual(fuel_capacity, self.testing_car.fuel_capacity)

    def test_car_fuel_capacity_setter__when_equal_to_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_capacity_setter__when_smaller_than_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.fuel_capacity = -1
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(context.exception))

    def test_car_fuel_amount__expect_to_return_fuel_amount(self):
        fuel_amount = 25
        self.testing_car.fuel_amount = 25
        self.assertEqual(fuel_amount, self.testing_car.fuel_amount)

    def test_car_fuel_amount_setter__when_smaller_than_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(context.exception))

    def test_car_refuel__when_given_fuel_is_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_given_fuel_is_smaller_than_zero__expect_Exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(context.exception))

    def test_car_refuel__when_given_fuel_is_correct__expect_to_increase_fuel_amount_by_given_fuel(self):
        given_fuel = 5
        self.testing_car.refuel(given_fuel)
        self.assertEqual(given_fuel, self.testing_car.fuel_amount)

    def test_car_refuel__when_fuel_amount_is_more_than_fuel_capacity__expect_to_increase_fuel_amount_to_fuel_capacity(
            self):
        self.testing_car.refuel(self.testing_car.fuel_capacity * 2)
        self.assertEqual(self.testing_car.fuel_amount, self.testing_car.fuel_capacity)

    def test_car_drive__when_needed_fuel_is_less_than_fuel_amount__expect_exception(self):
        with self.assertRaises(Exception) as context:
            self.testing_car.drive(1)
        self.assertEqual("You don't have enough fuel to drive!", str(context.exception))

    def test_car_drive__when_enough_fuel___expect_to_decrease_fuel_amount(self):
        self.testing_car.refuel(self.testing_car.fuel_capacity)
        distance = 300
        self.testing_car.drive(distance)
        needed = (distance / 100) * self.testing_car.fuel_consumption
        expected = self.testing_car.fuel_capacity - needed
        current = self.testing_car.fuel_amount
        self.assertEqual(current, expected)


if __name__ == '__main__':
    unittest.main()
