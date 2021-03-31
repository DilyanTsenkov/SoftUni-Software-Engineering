import unittest

from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    expected_fuel = 10.0
    expected_horse_power = 100.0

    def setUp(self):
        self.test_vehicle = Vehicle(self.expected_fuel, self.expected_horse_power)

    def test_vehicle_fuel__expect_to_be_float(self):
        self.assertTrue(isinstance(self.test_vehicle.fuel, float))

    def test_vehicle_horse_power__expect_to_be_float(self):
        self.assertTrue(isinstance(self.test_vehicle.horse_power, float))

    def test_vehicle_fuel_consumption__expect_to_be_float(self):
        self.assertTrue(isinstance(self.test_vehicle.fuel_consumption, float))

    def test_vehicle_init__when_correct_input_expect_be_initialized(self):
        self.assertEqual(self.expected_fuel, self.test_vehicle.fuel)
        self.assertEqual(self.expected_horse_power, self.test_vehicle.horse_power)
        self.assertEqual(self.test_vehicle.fuel, self.test_vehicle.capacity)
        self.assertEqual(Vehicle.DEFAULT_FUEL_CONSUMPTION, self.test_vehicle.fuel_consumption)

    def test_vehicle_drive__when_not_enough_fuel__expect_exception(self):
        with self.assertRaises(Exception) as context:
            kilometers = 9
            self.test_vehicle.drive(kilometers)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_vehicle_drive__when_enough_fuel__expect_fuel_to_decrease_with_fuel_need(self):
        kilometers = 5
        fuel_needed = self.test_vehicle.fuel_consumption * kilometers
        expected = self.test_vehicle.fuel - fuel_needed
        self.test_vehicle.drive(kilometers)
        self.assertEqual(self.test_vehicle.fuel, expected)

    def test_vehicle_refuel__when_not_enough_capacity__expect_exception(self):
        given_fuel = self.test_vehicle.capacity * 2
        with self.assertRaises(Exception) as context:
            self.test_vehicle.refuel(given_fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_vehicle_refuel__when_enough_capacity__expect_fuel_to_increase_with_fuel_added(self):
        self.test_vehicle.drive(4)
        given_fuel = 3
        expected = self.test_vehicle.fuel + given_fuel
        self.test_vehicle.refuel(given_fuel)
        self.assertEqual(self.test_vehicle.fuel, expected)

    def test_vehicle_str__expect_info(self):
        horse_power = self.test_vehicle.horse_power
        fuel = self.test_vehicle.fuel
        fuel_consumption = self.test_vehicle.fuel_consumption
        expect = f"The vehicle has {horse_power} " \
                 f"horse power with {fuel} fuel left and {fuel_consumption} fuel consumption"
        current = self.test_vehicle.__str__()
        self.assertEqual(current, expect)


if __name__ == '__main__':
    unittest.main()
