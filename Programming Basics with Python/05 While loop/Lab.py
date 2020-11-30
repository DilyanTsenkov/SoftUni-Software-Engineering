# ------------------------------------------------------09. Moving
width_free_space = int(input())
length_free_space = int(input())
high_free_space = int(input())
free_space_volume = width_free_space * length_free_space * high_free_space
packages_volume = 0
difference = 0
while free_space_volume >= packages_volume:
    package = input()
    if package == 'Done':
        print(f'{difference} Cubic meters left.')
        break
    packages_volume += int(package)
    difference = abs(free_space_volume - packages_volume)
if free_space_volume < packages_volume:
    print(f'No more free space! You need {difference} Cubic meters more.')
# ------------------------------------------------------08. Graduation pt.2
student_name = input()
level = 1
score_sum = 0
average = 0
while level <= 12:
    score = float(input())
    if score < 4:
        score = float(input())
        if score < 4:
            print(f'{student_name} has been excluded at {level} grade')
            break
    score_sum += score
    if level == 12:
        average = score_sum / level
        print(f'{student_name} graduated. Average grade: {average:.2f}')
    level += 1
# ------------------------------------------------------07. Min Number
input_text = input()
smallest_input = int(input_text)
while input_text != 'Stop':
    if int(input_text) < smallest_input:
        smallest_input = int(input_text)
    input_text = input()
print(smallest_input)
# ------------------------------------------------------06. Max Number
input_text = input()
biggest_input = int(input_text)
while input_text != 'Stop':
    if int(input_text) > biggest_input:
        biggest_input = int(input_text)
    input_text = input()
print(biggest_input)
# ------------------------------------------------------05. Account Balance
income = input()
total = 0
while income != 'NoMoreMoney':
    if float(income) < 0:
        print('Invalid operation!')
        break
    print(f'Increase: {float(income):.2f}')
    total += float(income)
    income = input()
print(f'Total: {total:.2f}')
# ------------------------------------------------------04. Sequence 2k+1
n = int(input())
number = 1
while number <= n:
    print(number)
    number = number * 2 + 1
# ------------------------------------------------------03. Sum Numbers
number = int(input())
sum_number = 0
while sum_number < number:
    input_number = int(input())
    sum_number += input_number
print(sum_number)
# ------------------------------------------------------02. Password
username = input()
password = input()
input_password = input()
while password != input_password:
    input_password = input()
print(f'Welcome {username}!')
# ------------------------------------------------------01. Read Text
text = input()
while text != 'Stop':
    print(text)
    text = input()
