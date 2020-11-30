class Class:
    __students_count = 22

    def __init__(self, name):
        self.name = name
        self.students = []
        self.grades = []

    def add_student(self, name, grade):
        self.student_name = name
        self.grade = grade
        if len(self.students) < Class.__students_count:
            self.students.append(self.student_name)
            self.grades.append(self.grade)
        self.students_string = ", ".join(self.students)

    def get_average_grade(self):
        grades_sum = sum(self.grades)
        average = grades_sum / len(self.grades)
        formatted_average = f"{average:.2f}"
        return float(formatted_average)


    def __repr__(self):
        return f"The students in {self.name}: {self.students_string}. Average grade: {(Class.get_average_grade(self))}"


a_class = Class("11B")
a_class.add_student("Peter", 4.80)
a_class.add_student("George", 6.00)
a_class.add_student("Amy", 3.50)

print(a_class)
