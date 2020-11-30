# -----------------------------------------------06. Salary
n = int(input())
salary = float(input())
for n in range(0, n):
    website = input()
    if website == "Facebook":
        salary -= 150
    elif website == "Instagram":
        salary -= 100
    elif website == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(f"{salary:.0f}")
# -----------------------------------------------05. Divide Without Remainder
n = int(input())
counter_two = 0
counter_three = 0
counter_four = 0
for number in range(1, n + 1):
    input_number = int(input())
    if input_number % 2 == 0:
        counter_two += 1
    if input_number % 3 == 0:
        counter_three += 1
    if input_number % 4 == 0:
        counter_four += 1
counter_two_percent = counter_two / n * 100
counter_three_percent = counter_three / n * 100
counter_four_percent = counter_four / n * 100
print(f"{counter_two_percent:.2f}%")
print(f"{counter_three_percent:.2f}%")
print(f"{counter_four_percent:.2f}%")
# -----------------------------------------------04. Histogram
n = int(input())
counter_one = 0
counter_two = 0
counter_three = 0
counter_four = 0
counter_five = 0
for number in range(1, n + 1):
    input_number = int(input())
    if input_number < 200:
        counter_one += 1
    elif 200 <= input_number < 400:
        counter_two += 1
    elif 400 <= input_number < 600:
        counter_three += 1
    elif 600 <= input_number < 800:
        counter_four += 1
    else:
        counter_five += 1
counter_one_percent = counter_one / n * 100
counter_two_percent = counter_two / n * 100
counter_three_percent = counter_three / n * 100
counter_four_percent = counter_four / n * 100
counter_five_percent = counter_five / n * 100
print(f"{counter_one_percent:.2f}%")
print(f"{counter_two_percent:.2f}%")
print(f"{counter_three_percent:.2f}%")
print(f"{counter_four_percent:.2f}%")
print(f"{counter_five_percent:.2f}%")
# -----------------------------------------------03. Odd / Even Position
n = int(input())
odd_sum = 0
odd_min = 2147483647
odd_max = -2147483647
even_sum = 0
even_min = 2147483647
even_max = -2147483647
for number in range(1, n + 1):
    input_number = float(input())
    if number % 2 == 1:
        odd_sum += input_number
        if input_number > odd_max:
            odd_max = input_number
        if input_number < odd_min:
            odd_min = input_number
    else:
        even_sum += input_number
        if input_number > even_max:
            even_max = input_number
        if input_number < even_min:
            even_min = input_number
print(f"OddSum={odd_sum:.2f},")
if odd_min == 2147483647:
    print("OddMin=No,")
    print("OddMax=No,")
else:
    print(f"OddMin={odd_min:.2f},")
    print(f"OddMax={odd_max:.2f},")
print(f"EvenSum={even_sum:.2f},")
if even_min == 2147483647:
    print("EvenMin=No,")
    print("EvenMax=No")
else:
    print(f"EvenMin={even_min:.2f},")
    print(f"EvenMax={even_max:.2f}")
# -----------------------------------------------02. Half Sum Element
n = int(input())
sum_of_all = 0
max_number = -2147483647
for number in range(0, n):
    input_number = int(input())
    if input_number > max_number:
        max_number = input_number
    sum_of_all += input_number
difference = abs(max_number - (sum_of_all - max_number))
if max_number == sum_of_all - max_number:
    print(f"Yes\nSum = {max_number}")
else:
    print(f"No\nDiff = {difference}")
# -----------------------------------------------01. Numbers Ending in 7
for number in range(1, 1001):
    if number % 10 == 7:
        print(number)
