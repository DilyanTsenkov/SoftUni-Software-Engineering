students = int(input())

students_data = {}

for _ in range(students):
    student, grade = input().split()
    grade = float(grade)
    if student not in students_data:
        students_data[student] = [grade]
    else:
        students_data[student].append(grade)

for key, value in students_data.items():
    grades = ""
    for grade in value:
        string = f"{grade:.2f} "
        grades += string
    print(f'{key} -> {grades}(avg: {(sum(value) / len(value)):.2f})')
