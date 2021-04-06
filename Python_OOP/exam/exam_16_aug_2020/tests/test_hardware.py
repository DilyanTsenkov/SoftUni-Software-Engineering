import unittest

from project.hardware.hardware import Hardware
from project.software.express_software import ExpressSoftware


class TestHardware(unittest.TestCase):
    NAME = "test name"
    TYPE = "Express"
    CAPACITY = 100
    MEMORY = 50

    def setUp(self):
        self.testing_hardware = Hardware(TestHardware.NAME, TestHardware.TYPE, TestHardware.CAPACITY,
                                         TestHardware.MEMORY)

    def test_hardware_name__expect_to_be_str(self):
        self.assertTrue(isinstance(TestHardware.NAME, str))

    def test_hardware_capacity__expect_to_be_int(self):
        self.assertTrue(isinstance(TestHardware.CAPACITY, int))

    def test_hardware_memory__expect_to_be_int(self):
        self.assertTrue(isinstance(TestHardware.MEMORY, int))

    def test_hardware_init__when_correct_input_expect_be_initialized(self):
        self.assertEqual(TestHardware.NAME, self.testing_hardware.name)
        self.assertEqual(TestHardware.TYPE, self.testing_hardware.type)
        self.assertEqual(TestHardware.CAPACITY, self.testing_hardware.capacity)
        self.assertEqual(TestHardware.MEMORY, self.testing_hardware.memory)
        self.assertEqual([], self.testing_hardware.software_components)

    def test_hardware_install__when_software_cannot_be_installed__expect_exception(self):
        express_software = ExpressSoftware("testing software", 100, 26)
        with self.assertRaises(Exception) as context:
            self.testing_hardware.install(express_software)
        self.assertEqual("Software cannot be installed", str(context.exception))

    def test_hardware_install__when_software_can_be_installed__expect_to_be_appended_in_software_components(self):
        express_software = ExpressSoftware("testing software", 100, 25)
        self.testing_hardware.install(express_software)
        self.assertEqual(1, len(self.testing_hardware.software_components))

    def test_hardware_uninstall__when_uninstall__expect_to_be_removed_from_software_components(self):
        express_software = ExpressSoftware("testing software", 100, 25)
        self.testing_hardware.install(express_software)
        self.testing_hardware.uninstall(express_software)
        self.assertEqual(0, len(self.testing_hardware.software_components))


if __name__ == '__main__':
    unittest.main()
