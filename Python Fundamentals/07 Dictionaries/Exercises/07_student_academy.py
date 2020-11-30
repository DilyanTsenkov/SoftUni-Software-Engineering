n = int(input())

students_database = {}
students_grade_counter = {}

for i in range(n):
    name = input()
    grade = float(input())

    if name not in students_database:
        students_database[name] = grade
        students_grade_counter[name] = 1
    else:
        students_database[name] += grade
        students_grade_counter[name] += 1

students_database = {name: grade / students_grade_counter[name] for name, grade in students_database.items()}
students_database = {name: grade for name, grade in students_database.items() if students_database[name] >= 4.5}

students_database = dict(sorted(students_database.items(), key=lambda x: x[1], reverse=True))

for name, grade in students_database.items():
    print(f"{name} -> {students_database[name]:.2f}")
