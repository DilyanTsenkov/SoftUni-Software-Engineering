# --------------------------------------------------07. Toy Shop
price_excursion = float(input())
puzzles = int(input())
dolls = int(input())
teddy_bears = int(input())
minions = int(input())
trucks = int(input())
puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2
profit = puzzles * puzzle_price + dolls * doll_price + teddy_bears * teddy_bear_price + minions * minion_price + trucks * truck_price
toys_count = puzzles + dolls + teddy_bears + minions + trucks
if toys_count >= 50:
    profit = profit - (profit * 0.25)
profit_and_rent = profit - (profit * 0.1)
result = profit_and_rent - price_excursion
if result >= 0:
    print(f'Yes! {result:.2f} lv left.')
else:
    print(f'Not enough money! {abs(result):.2f} lv needed.')
# --------------------------------------------------06. Area of Figures
import math

shape = input()
area = 0
if shape == 'square':
    a = float(input())
    area = a * a
elif shape == 'rectangle':
    a = float(input())
    b = float(input())
    area = a * b
elif shape == 'circle':
    r = float(input())
    area = math.pi * (r * r)
elif shape == 'triangle':
    a = float(input())
    ha = float(input())
    area = a * ha / 2
print(f'{area:.3f}')
# --------------------------------------------------05. Password Guess
password = input()
result = ''
if password == 's3cr3t!P@ssw0rd':
    result = 'Welcome'
else:
    result = 'Wrong password!'
print(result)
# --------------------------------------------------04. Number 100...200
number = int(input())
result = ''
if number < 100:
    result = 'Less than 100'
elif 100 <= number <= 200:
    result = 'Between 100 and 200'
elif number > 200:
    result = 'Greater than 200'
print(result)
# --------------------------------------------------03. Even or Odd
number = int(input())
result = ''
if number % 2 == 0:
    result = 'even'
else:
    result = 'odd'
print(result)
# --------------------------------------------------02. Greater Number
first_number = int(input())
second_number = int(input())
result = 0
if first_number >= second_number:
    result = first_number
else:
    result = second_number
print(result)
# --------------------------------------------------01. Excellent Result
grade = float(input())
if grade >= 5.50:
    print('Excellent!')
