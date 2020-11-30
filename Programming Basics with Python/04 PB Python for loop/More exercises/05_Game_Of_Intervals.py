turns = int(input())
result = 0
invalid_count = 0
first_count = 0
second_count = 0
third_count = 0
fourth_count = 0
fifth_count = 0
for turn in range(0, turns):
    number = int(input())
    if number < 0 or number > 50:
        result = result / 2
        invalid_count += 1
    elif 0 <= number <= 9:
        result += number * 0.2
        first_count += 1
    elif 10 <= number <= 19:
        result += number * 0.3
        second_count += 1
    elif 20 <= number <= 29:
        result += number * 0.4
        third_count += 1
    elif 30 <= number <= 39:
        result += 50
        fourth_count += 1
    elif 40 <= number <= 50:
        result += 100
        fifth_count += 1
first_percent = first_count / turns * 100
second_percent = second_count / turns * 100
third_percent = third_count / turns * 100
fourth_percent = fourth_count / turns * 100
fifth_percent = fifth_count / turns * 100
invalid_percent = invalid_count / turns * 100
print(f'{result:.2f}')
print(f'From 0 to 9: {first_percent:.2f}%')
print(f'From 10 to 19: {second_percent:.2f}%')
print(f'From 20 to 29: {third_percent:.2f}%')
print(f'From 30 to 39: {fourth_percent:.2f}%')
print(f'From 40 to 50: {fifth_percent:.2f}%')
print(f'Invalid numbers: {invalid_percent:.2f}%')