database = {}

while True:
    course_student = input()
    if course_student == "end":
        break

    course_name, student_name = course_student.split(" : ")

    if course_name not in database:
        database[course_name] = []
        database[course_name].append(student_name)
    else:
        database[course_name].append(student_name)

database = dict(sorted(database.items(), key=lambda v: len(v[1]), reverse=True))

for key in database:
    database[key].sort()

for course, students in database.items():
    print(f"{course}: {len(students)}")
    for el in students:
        print(f"-- {el}")
