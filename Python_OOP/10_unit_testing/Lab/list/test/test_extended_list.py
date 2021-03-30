import unittest

# from list.extended_list import IntegerList


class TestIntegerList(unittest.TestCase):

    def test_integer_list_init__when_int__expect_to_create_it(self):
        int_list = IntegerList(1, 2, "not integer", 3)
        current = int_list.get_data()
        expected = [1, 2, 3]
        self.assertEqual(current, expected)

    def test_integer_list_add__when_int__expect_to_add_it(self):
        int_list = IntegerList(1, 2, 3)
        test_list = int_list.add(7)
        expected = [1, 2, 3, 7]
        self.assertEqual(expected, test_list)

    def test_integer_list_add__when_str__expect_exception(self):
        int_list = IntegerList()
        with self.assertRaises(ValueError):
            int_list.add("not integer")

    def test_integer_list_remove__when_valid_index__expect_to_return_index(self):
        to_remove = 3
        int_list = IntegerList(1, 2, to_remove, 4)
        result_index = int_list.remove_index(2)
        self.assertEqual(to_remove, result_index)

    def test_integer_list_remove__when_invalid_index__expect_to_return_exception(self):
        int_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            int_list.remove_index(index)

    def test_integer_list_get__when_valid_index__expect_to_return_element(self):
        to_get = 3
        int_list = IntegerList(1, 2, to_get, 4)
        result_index = int_list.get(2)
        self.assertEqual(to_get, result_index)

    def test_integer_list_get__when_invalid_index__expect_to_return_exception(self):
        int_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            int_list.get(index)

    def test_integer_list_insert__expect_to_insert_element(self):
        int_list = IntegerList(1, 2, 3)
        int_list.insert(0, 7)
        current = int_list.get_data()
        expect = [7, 1, 2, 3]
        self.assertEqual(current, expect)

    def test_integer_list_insert__when_invalid_index__expect_to_return_exception(self):
        int_list = IntegerList(1, 2, 3)
        index = 3
        with self.assertRaises(IndexError):
            int_list.insert(index, 1)

    def test_integer_list_insert__when_str_el__expect_to_return_exception(self):
        int_list = IntegerList(1, 2, 3)
        element = "not integer"
        with self.assertRaises(ValueError):
            int_list.insert(2, element)

    def test_integer_list_get_biggest__expect_to_return_biggest(self):
        expect = 6
        int_list = IntegerList(1, 2, expect, 3)
        current = int_list.get_biggest()
        self.assertEqual(current, expect)

    def test_integer_list_get_index__expect_to_return_index_of_element(self):
        int_list = IntegerList(1, 2, 6, 3)
        current = int_list.get_index(6)
        expect = 2
        self.assertEqual(current, expect)


if __name__ == '__main__':
    unittest.main()
