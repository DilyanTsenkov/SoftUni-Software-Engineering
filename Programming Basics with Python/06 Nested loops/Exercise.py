# --------------------------------------------- 06. Special Numbers
N = int(input())
for number in range(1111, 10000):
    counter = 0
    for digit in str(number):
        if int(digit) == 0:
            break
        elif N % int(digit) == 0:
            counter += 1
    if counter == 4:
        print(number, end=" ")
# ----------------------------------------
N = int(input())
for number in range(1111, 10000):
    current_number = number
    counter = 0
    for i in range(4):
        last = current_number % 10
        if last == 0:
            break
        else:
            if N % last == 0:
                counter += 1
        current_number = current_number // 10
    if counter == 4:
        print(number, end=" ")
# ----------------------------------------------
n = int(input())
for first_symbol in range(1, 10):
    for second_symbol in range(1, 10):
        for third_symbol in range(1, 10):
            for fourth_symbol in range(1, 10):
                if n % first_symbol == 0 and n % second_symbol == 0 and n % third_symbol == 0 and n % fourth_symbol == 0:
                    print(f"{first_symbol}{second_symbol}{third_symbol}{fourth_symbol}", end=' ')
# --------------------------------------------- 05. Password Generator
n = int(input())
l = int(input())
for first_symbol in range(1, n + 1):
    for second_symbol in range(1, n + 1):
        for third_symbol in range(ord("a"), (96 + l + 1)):
            for fourth_symbol in range(ord("a"), (96 + l + 1)):
                for fifth_symbol in range((max(first_symbol, second_symbol) + 1), n + 1):
                    print(f"{first_symbol}{second_symbol}{chr(third_symbol)}{chr(fourth_symbol)}{fifth_symbol}",
                          end=' ')
# --------------------------------------------- 04. Train The Trainers
judges = int(input())
average_grade_all = 0
presentation_counter = 0
while True:
    presentation = input()
    grade_sum = 0
    if presentation == "Finish":
        print(f"Student's final assessment is {(average_grade_all / presentation_counter):.2f}.")
        break
    presentation_counter += 1
    for grades in range(0, judges):
        grade = float(input())
        grade_sum += grade
        average_grade_pr = grade_sum / judges
    print(f"{presentation} - {average_grade_pr:.2f}.")
    average_grade_all += average_grade_pr
# --------------------------------------------- 03. Sum Prime Non Prime
prime_numbers_sum = 0
non_prime_numbers_sum = 0
while True:
    number = input()
    check = 0
    if number == "stop":
        break
    elif int(number) < 0:
        print("Number is negative.")
        continue
    for num in range(1, int(number) + 1):
        if int(number) % num == 0:
            check += 1
    if check == 2:
        prime_numbers_sum += int(number)
    else:
        non_prime_numbers_sum += int(number)
print(f"Sum of all prime numbers is: {prime_numbers_sum}\nSum of all non prime numbers is: {non_prime_numbers_sum}")
# --------------------------------------------- 02. Equal Sums Even Odd Position
number_one = int(input())
number_two = int(input())
for number in range(number_one, number_two + 1):
    current_number = number
    odd_sum = 0
    even_sum = 0
    for even_odd in range(1, 7):
        last_digit = current_number % 10
        current_number = current_number // 10
        if even_odd % 2 == 0:
            even_sum += last_digit
        else:
            odd_sum += last_digit
    if odd_sum == even_sum:
        print(number, end=" ")
# -------------With ENUMERATE ------------With ENUMERATE ---------With ENUMERATE ---------With ENUMERATE
number_one = int(input())
number_two = int(input())
for number in range(number_one, number_two + 1):
    current_number = str(number)
    even_sum = 0
    odd_sum = 0
    for index, digit in enumerate(current_number):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)
    if odd_sum == even_sum:
        print(current_number, end=" ")
# --------------------------------------------- 01. Number Pyramid
n = int(input())
number = 0
breaker = False
for row in range(1, n + 1):
    for col in range(1, row + 1):
        number += 1
        print(number, end=" ")
        if number == n:
            breaker = True
            break
    if breaker:
        break
    print()
