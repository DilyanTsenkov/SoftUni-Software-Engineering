# ----------------------------------------------------07. Cinema Tickets
sold_tickets = 0
student_tickets = 0
standard_tickets = 0
kids_tickets = sold_tickets - standard_tickets - student_tickets
while True:
    movie = input()
    if movie == "Finish":
        break
    places = int(input())
    free_places = places
    while True:
        full_percent = 100 - (free_places / places * 100)
        if free_places == 0:
            print(f"{movie} - {full_percent:.2f}% full.")
            break
        ticket = input()
        if ticket == "End":
            print(f"{movie} - {full_percent:.2f}% full.")
            break
        elif ticket == "student":
            student_tickets += 1
        elif ticket == "standard":
            standard_tickets += 1
        sold_tickets += 1
        free_places -= 1
student_tickets_percent = student_tickets / sold_tickets * 100
standard_tickets_percent = standard_tickets / sold_tickets * 100
kids_tickets_percent = 100 - student_tickets_percent - standard_tickets_percent
print(f"Total tickets: {sold_tickets}\n{student_tickets_percent:.2f}% student tickets.")
print(f"{standard_tickets_percent:.2f}% standard tickets.\n{kids_tickets_percent:.2f}% kids tickets.")
# ----------------------------------------------------06. Building
floors = int(input())
rooms_on_floor = int(input())
for floor in range(floors, 0, -1):
    for room in range(0, rooms_on_floor):
        if floor == floors:
            print(f"L{floor}{room} ", end="")
        elif floor % 2 == 0:
            print(f"O{floor}{room} ", end="")
        elif floor % 2 == 1:
            print(f"A{floor}{room} ", end="")
    print()
# ----------------------------------------------------05. Travelling
money_in_bank = 0
while True:
    destination = input()
    if destination == "End":
        break
    min_budget = float(input())
    while True:
        save_money = input()
        money_in_bank += float(save_money)
        if min_budget <= money_in_bank:
            print(f"Going to {destination}!")
            money_in_bank = 0
            break
# ----------------------------------------------------04. Sum of Two Numbers
interval_start = int(input())
interval_end = int(input())
magic_number = int(input())
sum_numbers = 0
counter = 0
for number_one in range(interval_start, interval_end + 1):
    for number_two in range(interval_start, interval_end + 1):
        sum_numbers = number_one + number_two
        counter += 1
        if sum_numbers == magic_number:
            print(f"Combination N:{counter} ({number_one} + {number_two} = {magic_number})")
            break
    if sum_numbers == magic_number:
        break
if sum_numbers != magic_number:
    print(f"{counter} combinations - neither equals {magic_number}")
# ----------------------------------------------------03. Combinations
n = int(input())
counter = 0
for x_1 in range(0, n + 1):
    for x_2 in range(0, n + 1):
        for x_3 in range(0, n + 1):
            if x_1 + x_2 + x_3 == n:
                counter += 1
print(counter)
# ----------------------------------------------------02. Multiplication Table
for multiplier_one in range(1, 11):
    for multiplier_two in range(1, 11):
        result = multiplier_one*multiplier_two
        print(f"{multiplier_one} * {multiplier_two} = {result}")
# ----------------------------------------------------01. Clock
for hour in range(0, 24):
    for minute in range(0, 60):
        print(f"{hour}:{minute}")
