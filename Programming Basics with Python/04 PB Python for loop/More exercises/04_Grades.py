students = int(input())
poor_grades = 0
poor_grades_sum = 0
average_grades = 0
average_grades_sum = 0
good_grades = 0
good_grades_sum = 0
very_good_grades = 0
very_good_grades_sum = 0
for student in range(0, students):
    grade = float(input())
    if 2 <= grade <= 2.99:
        poor_grades += 1
        poor_grades_sum += grade
    elif 3 <= grade <= 3.99:
        average_grades += 1
        average_grades_sum += grade
    elif 4 <= grade <= 4.99:
        good_grades += 1
        good_grades_sum += grade
    elif grade >= 5:
        very_good_grades += 1
        very_good_grades_sum += grade
average = (poor_grades_sum + average_grades_sum + good_grades_sum + very_good_grades_sum) / students
poor_grades_percent = poor_grades / students * 100
average_grades_percent = average_grades / students * 100
good_grades_percent = good_grades / students * 100
very_good_grades_percent = very_good_grades / students * 100
print(f'Top students: {very_good_grades_percent:.2f}%')
print(f'Between 4.00 and 4.99: {good_grades_percent:.2f}%')
print(f'Between 3.00 and 3.99: {average_grades_percent:.2f}%')
print(f'Fail: {poor_grades_percent:.2f}%')
print(f'Average: {average:.2f}')
