first_employee_can_help = int(input())
second_employee_can_help = int(input())
third_employee_can_help = int(input())
students = int(input())

all_employees_can_help = first_employee_can_help + second_employee_can_help + third_employee_can_help
hours = 0

while students > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    students -= all_employees_can_help

print(f"Time needed: {hours}h.")
