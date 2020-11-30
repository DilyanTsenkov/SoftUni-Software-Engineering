first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_people = int(input())

people_per_hour = first_employee + second_employee + third_employee
time_needed = 0

while total_people > 0:
    time_needed += 1
    if time_needed % 4 == 0 and time_needed != 0:
        continue
    total_people -= people_per_hour

print(f"Time needed: {time_needed}h.")
