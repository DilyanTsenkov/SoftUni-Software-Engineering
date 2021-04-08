import unittest
from project.factory.paint_factory import PaintFactory


class TestFactory(unittest.TestCase):
    NAME = "test name"
    CAPACITY = 100
    INGREDIENTS = {}
    VALID_INGREDIENTS = ["white", "yellow", "blue", "green", "red"]

    def setUp(self):
        self.testing_factory = PaintFactory(TestFactory.NAME, TestFactory.CAPACITY)

    def test_factory_name__expect_to_be_str(self):
        self.assertTrue(isinstance(TestFactory.NAME, str))

    def test_factory_capacity__expect_to_be_int(self):
        self.assertTrue(isinstance(TestFactory.CAPACITY, int))

    def test_factory_ingredients__expect_to_be_dict(self):
        self.assertTrue(isinstance(TestFactory.INGREDIENTS, dict))

    def test_factory_init__when_correct_input_expect_be_initialized(self):
        self.assertEqual(TestFactory.NAME, self.testing_factory.name)
        self.assertEqual(TestFactory.CAPACITY, self.testing_factory.capacity)
        self.assertEqual(TestFactory.INGREDIENTS, self.testing_factory.ingredients)
        self.assertEqual(TestFactory.INGREDIENTS, self.testing_factory.products)

    def test_factory_add_ingredient__when_try_to_add_not_valid_ingredient__expect_type_error(self):
        ingredient_type = "orange"
        quantity = 3
        with self.assertRaises(TypeError) as context:
            self.testing_factory.add_ingredient(ingredient_type, quantity)
        self.assertEqual(f"Ingredient of type {ingredient_type} not allowed in PaintFactory", str(context.exception))

    def test_factory_add_ingredient__when_not_enough_capacity__expect_value_error(self):
        ingredient_type = "white"
        quantity = 101
        with self.assertRaises(ValueError) as context:
            self.testing_factory.add_ingredient(ingredient_type, quantity)
        self.assertEqual("Not enough space in factory", str(context.exception))

    def test_factory_add_ingredient__expect_to_increase_ingredient_type_with_quantity(self):
        ingredient_type = "white"
        quantity = 5
        self.testing_factory.add_ingredient(ingredient_type, quantity)
        self.assertEqual({ingredient_type: quantity}, self.testing_factory.ingredients)

    def test_factory_remove_ingredient__when_try_to_remove_ingredient_that_is_not_in_ingredients_keys__expect_key_error(
            self):
        ingredient_type = "orange"
        quantity = 5
        with self.assertRaises(KeyError) as context:
            self.testing_factory.remove_ingredient(ingredient_type, quantity)
        self.assertEqual("No such ingredient in the factory", context.exception.args[0])

    def test_factory_remove_ingredient__when_try_to_remove_more_quantity_that_exist__expect_value_error(self):
        ingredient_type = "white"
        quantity = 5
        self.testing_factory.add_ingredient(ingredient_type, quantity)
        quantity_to_remove = 6
        with self.assertRaises(ValueError) as context:
            self.testing_factory.remove_ingredient(ingredient_type, quantity_to_remove)
        self.assertEqual("Ingredient quantity cannot be less than zero", str(context.exception))

    def test_factory_remove_ingredient__expect_to_decrease_ingredient_type_quantity(self):
        ingredient_type = "white"
        quantity = 5
        self.testing_factory.add_ingredient(ingredient_type, quantity)
        quantity_to_remove = 4
        self.testing_factory.remove_ingredient(ingredient_type, quantity_to_remove)
        self.assertEqual(1, self.testing_factory.ingredients[ingredient_type])

    def test_factory_products__expect_dict_of_ingredients(self):
        ingredient_type = "white"
        quantity = 5
        self.testing_factory.add_ingredient(ingredient_type, quantity)
        quantity_to_remove = 4
        self.testing_factory.remove_ingredient(ingredient_type, quantity_to_remove)
        self.assertEqual({'white': 1}, self.testing_factory.products)


if __name__ == '__main__':
    unittest.main()
