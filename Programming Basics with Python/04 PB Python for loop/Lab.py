# -----------------------------------------11. Clever Lily
age = int(input())
laundry_machine_price = float(input())
toy_prise = int(input())
present_toy = 0
money = 0
for birthday in range(1, age + 1):
    if birthday % 2 == 1:
        present_toy += 1
    else:
        money += 10 * birthday // 2
        money -= 1
money_from_present_toy = present_toy * toy_prise
total_money = money + money_from_present_toy
result = abs(total_money - laundry_machine_price)
if total_money >= laundry_machine_price:
    print(f"Yes! {result:.2f}")
else:
    print(f"No! {result:.2f}")
# -----------------------------------------10. Odd Even Sum
n = int(input())
even_sum = 0
odd_sum = 0
for number in range(0, n):
    input_number = int(input())
    if number % 2 == 0:
        even_sum += input_number
    else:
        odd_sum += input_number
difference = abs(even_sum - odd_sum)
if even_sum == odd_sum:
    print(f"Yes\nSum = {even_sum}")
else:
    print(f"No\nDiff = {difference}")
# -----------------------------------------09. Left and Right Sum
n = int(input())
left_sum = 0
right_sum = 0
for numbers in range(0, n):
    left_number = int(input())
    left_sum += left_number
for numbers in range(n + 1, 2 * n + 1):
    right_number = int(input())
    right_sum += right_number
difference = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
# -----------------------------------------08. Number sequence
n = int(input())
max_number = -2147483647
min_number = 2147483647
for numbers in range(n):
    new_number = int(input())
    if new_number >= max_number:
        max_number = new_number
    if new_number <= min_number:
        min_number = new_number
print(f"Max number: {max_number}\nMin number: {min_number}")
# -----------------------------------------07. Sum Numbers
n = int(input())
result = 0
for numbers in range(n):
    new_number = int(input())
    result += new_number
print(result)
# -----------------------------------------06. Vowels Sum
text = input()
result = 0
for letter in text:
    if letter == "a":
        result += 1
    elif letter == "e":
        result += 2
    elif letter == "i":
        result += 3
    elif letter == "o":
        result += 4
    elif letter == "u":
        result += 5
print(result)
# -----------------------------------------05. Character Sequence
text = input()
for letter in text:
    print(letter)
# -----------------------------------------04. Even Powers of 2
n = int(input())
result = 0
for number in range(0, n + 1, 2):
    result = 2 ** number
    print(result)
# -----------------------------------------03. Numbers 1...N with Step 3
n = int(input())
for numbers in range(1, n+1, 3):
    print(numbers)
# -----------------------------------------02. Numbers N...1
n = int(input())
for numbers in range(n, 0, -1):
    print(numbers)
# -----------------------------------------01. Numbers from 1 to 100
for numbers in range(1, 101):
    print(numbers)
