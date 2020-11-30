#----------------------------------------------------------------------------------06. Exam Results
student_name = input()
while student_name != "Midnight":
    collected_point = 0
    for task in range(6):
        points = int(input())
        if points < 0:
            break
        collected_point += points
    final_points = int(collected_point / 600 * 100)
    grade = final_points * 0.06
    if points < 0:
        print(f"{student_name} was cheating!")
    elif 0 <= grade <= 2:
        print(f"{student_name} - 2.00")
    elif grade <= 5:
        print(f"{student_name} - {grade:.2f}")
    else:
        print("===================")
        print("|   CERTIFICATE   |")
        print(f"|    {grade:.2f}/6.00    |")
        print("===================")
        print(f"Issued to {student_name}")
    student_name = input()
#----------------------------------------------------------------------------------05. Exam Preparation
students = int(input())
tasks = int(input())
energy = int(input())
task_counter = 0
question_counter = 0
while energy > 0:
    energy = energy + tasks * 2
    students -= tasks
    questions = students * 2
    energy = energy - questions * 3
    task_counter += tasks
    question_counter += questions
    if students < 10:
        print("The students are too few!")
        print(f"Problems solved: {task_counter}")
        break
    if energy <= 0:
        print(f"The trainer is too tired!")
        print(f"Questions asked: {question_counter}")
    add_students = students // 10
    students += add_students
#----------------------------------------------------------------------------------04. Exam Retention
import math

students = int(input())
seasons = int(input())
for season in range(1, seasons + 1):
    first_exam = math.ceil(students * 0.9)
    second_exam = math.ceil(first_exam * 0.9)
    proceed = math.ceil(second_exam * 0.8)
    if season % 3 == 0:
        re_signed = math.ceil(proceed * 0.15)
    else:
        re_signed = math.ceil(proceed * 0.05)
    students = proceed + re_signed
print(f"Students: {students}")
#----------------------------------------------------------------------------------03. Exam Categories
complexity = int(input())
unclear = int(input())
pages = int(input())
if complexity >= 80 and unclear >= 80 and pages >= 8:
    result = "Legacy"
elif complexity >= 80 and unclear <= 10:
    result = "Master"
elif 10 < complexity <= 30 and pages <= 1:
    result = "Easy"
elif complexity <= 10:
    result = "Elementary"
elif unclear >= 50 and pages >= 2:
    result = "Hard"
else:
    result = "Regular"
print(result)
#----------------------------------------------------------------------------------02. Exam Points
tasks = int(input())
points = int(input())
level = input()
if level == "Basics":
    if tasks == 1:
        result = points * 0.08
    elif tasks == 2:
        result = points * 0.09
    elif tasks == 3:
        result = points * 0.09
    else:
        result = points * 0.1
elif level == "Fundamentals":
    if tasks == 1:
        result = points * 0.11
    elif tasks == 2:
        result = points * 0.11
    elif tasks == 3:
        result = points * 0.12
    else:
        result = points * 0.13
else:
    if tasks == 1:
        result = points * 0.14
    elif tasks == 2:
        result = points * 0.14
    elif tasks == 3:
        result = points * 0.15
    else:
        result = points * 0.16
if level == "Advanced":
    result *= 1.2
if tasks == 1 and level == "Basics":
    result *= 0.8
print(f"Total points: {result:.2f}")

#----------------------------------------------------------------------------------01. Exam Submissions
import math

students = int(input())
tasks = int(input())
submission = students * math.ceil(tasks * 2.8)
three_tasks = students * (tasks // 3)
total_submission = submission + three_tasks
memory = 5 * math.ceil(total_submission / 10)
print(f"{memory} KB needed")
print(f"{total_submission} submissions")
