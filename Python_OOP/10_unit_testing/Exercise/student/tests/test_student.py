import unittest

from project.student import Student


class TestStudent(unittest.TestCase):

    def test_student_init__when_name_is_str_and_courses_is_none__expect_to_be_initialized_with_empty_dict(self):
        test_student_name = "Test name"
        test_student_courses = None
        test_student = Student(test_student_name, test_student_courses)
        result = [test_student.name, test_student.courses]
        expect_result = ["Test name", {}]
        self.assertEqual(expect_result, result)

    def test_student_init__when_name_is_str_and_courses_is_dict__expect_to_be_initialized(self):
        test_student_name = "Test name"
        test_student_courses = {"course_name": ["notes"], "course_name 2": ["notes2"]}
        test_student = Student(test_student_name, test_student_courses)
        result = [test_student.name, test_student.courses]
        expect_result = ["Test name", {"course_name": ["notes"], "course_name 2": ["notes2"]}]
        self.assertEqual(expect_result, result)

    def test_student_name__expect_to_be_str(self):
        test_student_name = "Test name"
        test_student_courses = None
        test_student = Student(test_student_name, test_student_courses)
        self.assertTrue(isinstance(test_student.name, str))

    def test_student_enroll__if_course_name_in_course(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        test_student.enroll("test_course_name", ["test_notes", "test_notes2"], "Eureka")
        result_msg = test_student.enroll("test_course_name", ["test_notes", "test_notes2"], "Eureka")
        result = [test_student.name, test_student.courses, result_msg]
        expect = ["Test name", {"test_course_name": ["test_notes", "test_notes2"]},
                  "Course already added. Notes have been updated."]
        self.assertEqual(expect, result)

    def test_student_enroll__course_adding(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        result_msg = test_student.enroll("test_course_name", ["test_notes", "test_notes2"], "Eureka")
        result = [test_student.name, test_student.courses, result_msg]
        expect = ["Test name", {"test_course_name": []}, "Course has been added."]
        self.assertEqual(expect, result)

    def test_student_enroll__if_add_course_notes_equal_Y(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        result_msg = test_student.enroll("test_course_name", ["test_notes", "test_notes2"], "Y")
        result = [test_student.name, test_student.courses, result_msg]
        expect = ["Test name", {"test_course_name": ["test_notes", "test_notes2"]},
                  "Course and course notes have been added."]
        self.assertEqual(expect, result)

    def test_student_enroll__if_add_course_notes_equal_empty_str(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        result_msg = test_student.enroll("test_course_name", ["test_notes", "test_notes2"], "")
        result = [test_student.name, test_student.courses, result_msg]
        expect = ["Test name", {"test_course_name": ["test_notes", "test_notes2"]},
                  "Course and course notes have been added."]
        self.assertEqual(expect, result)


    def test_student_add_notes_to_existing_course(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        result = test_student.enroll("test_course_name", ["test_notes", "test_notes2"])
        result = test_student.enroll("test_course_name", ["test_notes3", "test_notes4"])
        length_of_courses = len(test_student.courses)
        expect_length_of_courses = 1
        self.assertEqual(expect_length_of_courses, length_of_courses)
        length_of_notes = len(test_student.courses["test_course_name"])
        expect_length_of_notes = 4
        self.assertEqual(expect_length_of_notes, length_of_notes)
        expect_result = "Course already added. Notes have been updated."
        self.assertEqual(expect_result, result)

    def test_student_add_notes_not_existing_course_raises(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        with self.assertRaises(Exception) as context:
            test_student.add_notes("test_course_name", ["test_notes", "test_notes2"])
        self.assertEqual("Cannot add notes. Course not found.", str(context.exception))

    def test_student_add_notes_with_existing_course(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        result = test_student.enroll("test_course_name", ["test_notes", "test_notes2"])
        result = test_student.add_notes("test_course_name", "Testing")
        length_of_notes = len(test_student.courses["test_course_name"])
        expect_length_of_notes = 3
        self.assertEqual(expect_length_of_notes, length_of_notes)
        expect_result = "Notes have been updated"
        self.assertEqual(expect_result, result)
        self.assertIn("Testing", test_student.courses["test_course_name"])

    def test_student_not_existing_course__raises(self):
        test_student_name = "Test name"
        test_student = Student(test_student_name)
        with self.assertRaises(Exception) as context:
            test_student.leave_course("test_course_name")
        self.assertEqual("Cannot remove course. Course not found.", str(context.exception))

    def test_student_leave_existing_course_(self):
        test_student_name = "Test name"
        test_student_courses = {"course_name": ["notes"]}
        test_student = Student(test_student_name, test_student_courses)
        result = test_student.leave_course("course_name")
        length_of_courses = len(test_student.courses)
        expect_length_of_courses = 0
        self.assertEqual(expect_length_of_courses, length_of_courses)
        expect_result = "Course has been removed"
        self.assertEqual(expect_result, result)


if __name__ == '__main__':
    unittest.main()
