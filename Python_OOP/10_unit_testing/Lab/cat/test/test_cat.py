import unittest

# from cat.cat import Cat


class TestCat(unittest.TestCase):
    name = "Test Cat"

    def setUp(self):
        self.test_cat = Cat(self.name)

    def test_cat_eat___expect_size_to_be_increased(self):
        """Cat's size is increased after eating"""
        self.test_cat.eat()
        self.assertEqual(1, self.test_cat.size)

    def test_cat_eat__expect_fed_to_be_true(self):
        """Cat is fed after eating"""
        self.test_cat.eat()
        self.assertTrue(self.test_cat.fed)

    def test_cat_eat__when_fed__expect_exception(self):
        """Cat cannot eat if already fed, raises an error"""
        self.test_cat.eat()
        with self.assertRaises(Exception):
            self.test_cat.eat()

    def test_cat_sleep__when_not_fed__expect_exception(self):
        """Cat cannot fall asleep if not fed, raises an error"""
        with self.assertRaises(Exception):
            self.test_cat.sleep()

    def test_cat_sleep__expect_not_to_be_sleepy_after(self):
        """Cat is not sleepy after sleeping"""
        self.test_cat.eat()
        self.test_cat.sleep()
        self.assertFalse(self.test_cat.sleepy)


if __name__ == '__main__':
    unittest.main()
