import unittest


# from worker.worker import Worker


class TestWorker(unittest.TestCase):
    name = "Test Worker"
    salary = 1000
    energy = 100

    def setUp(self):
        self.test_worker = Worker(self.name, self.salary, self.energy)

    def test_worker_init__when_correct_name_salary_energy_expect_be_initialized(self):
        """Test if the worker is initialized with correct name, salary and energy"""
        name = "Test Worker"
        salary = 1000
        energy = 100
        test_worker = Worker(name, salary, energy)

        self.assertEqual(self.name, test_worker.name)
        self.assertEqual(self.salary, test_worker.salary)
        self.assertEqual(self.energy, test_worker.energy)

    def test_worker_rest__expect_worker_energy_to_be_incremented(self):
        """Test if the worker's energy is incremented after the rest method is called"""
        self.test_worker.rest()
        self.assertEqual(self.energy + 1, self.test_worker.energy)

    def test_worker__when_worker_tries_to_work_with_0_energy__expect_exception(self):
        """Test if an error is raised if the worker tries to work with negative energy or equal to 0"""
        self.test_worker.energy = 0
        with self.assertRaises(Exception):
            self.test_worker.work()

    def test_worker__when_work__expect_worker_money_to_be_increased_by_salary(self):
        """Test if the worker's money is increased by his salary correctly after the work method is called"""
        self.test_worker.work()
        self.assertEqual(self.salary, self.test_worker.money)

    def test_worker__when_work__expect_worker_energy_to_be_decreased(self):
        """Test if the worker's energy is decreased after the work method is called"""
        self.test_worker.work()
        self.assertEqual(self.energy - 1, self.test_worker.energy)

    def test_worker_get_info__expect_to_return_correct_values(self):
        """Test if the get_info method returns the proper string with correct values"""
        expected_info = f'{self.name} has saved 0 money.'
        current_info = self.test_worker.get_info()
        self.assertEqual(expected_info, current_info)


if __name__ == '__main__':
    unittest.main()
