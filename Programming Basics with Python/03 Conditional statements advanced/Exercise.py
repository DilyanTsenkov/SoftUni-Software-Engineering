# ----------------------------------------------------09. Volleyball
import math

year = input()
p = int(input())
h = int(input())
saturday_play_in_sofia = ((48 - h) * 0.75) + (2 * p / 3)
total_days_played = saturday_play_in_sofia + h
if year == 'leap':
    total_days_played *= 1.15
print(math.floor(total_days_played))
# ----------------------------------------------------08. On Time for the Exam
exam_star_hour = int(input())
exam_star_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())
exam_star_in_minutes = exam_star_hour * 60 + exam_star_minutes
arrival_in_minutes = arrival_hour * 60 + arrival_minutes
late = arrival_in_minutes - exam_star_in_minutes
early = exam_star_in_minutes - arrival_in_minutes
if exam_star_in_minutes >= arrival_in_minutes >= exam_star_in_minutes - 30:
    print('On time')
    if early > 0:
        print(f'{early} minutes before the start')
elif arrival_in_minutes > exam_star_in_minutes:
    print('Late')
    if late < 60:
        print(f'{late} minutes after the start')
    else:
        print(f'{late // 60}:{(late % 60):02d} hours after the start')
else:
    print('Early')
    if early < 60:
        print(f'{early} minutes before the start')
    else:
        print(f'{early // 60}:{(early % 60):02d} hours before the start')
# ----------------------------------------------------07. Hotel Room
month = input()
nights = int(input())
if month == 'May' or month == 'October':
    studio = 50 * nights
    apartment = 65 * nights
    if 14 > nights > 7:
        studio *= 0.95
    if nights > 14:
        studio *= 0.7
elif month == 'June' or month == 'September':
    studio = 75.20 * nights
    apartment = 68.70 * nights
    if nights > 14:
        studio *= 0.80
elif month == 'July' or month == 'August':
    studio = 76 * nights
    apartment = 77 * nights
if nights > 14:
    apartment *= 0.9
print(f'Apartment: {apartment:.2f} lv.')
print(f'Studio: {studio:.2f} lv.')
# ----------------------------------------------------06. Operations Between Numbers
N1 = int(input())
N2 = int(input())
operator = input()
result = 0
if operator == '+':
    result = N1 + N2
elif operator == '-':
    result = N1 - N2
elif operator == '*':
    result = N1 * N2
elif operator == '/':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 / N2
        print(f'{N1} {operator} {N2} = {result:.2f}')
elif operator == '%':
    if N2 == 0:
        print(f'Cannot divide {N1} by zero')
    else:
        result = N1 % N2
        print(f'{N1} {operator} {N2} = {result}')
if operator == '+' or operator == '-' or operator == '*':
    if result % 2 == 0:
        print(f'{N1} {operator} {N2} = {result} - even')
    else:
        print(f'{N1} {operator} {N2} = {result} - odd')
# ----------------------------------------------------05. Journey
budget = float(input())
season = input()
place = 'Hotel'
destination = 'Bulgaria'
if budget <= 100:
    if season == 'summer':
        budget *= 0.3
        place = 'Camp'
    else:
        budget *= 0.7
elif budget <= 1000:
    destination = 'Balkans'
    if season == 'summer':
        budget *= 0.4
        place = 'Camp'
    else:
        budget *= 0.8
elif budget > 1000:
    destination = 'Europe'
    budget *= 0.9
print(f'Somewhere in {destination}')
print(f'{place} - {budget:.2f}')
# ----------------------------------------------------04. Fishing Boat
budget = int(input())
season = input()
fishermen = int(input())
price = 0
if season == 'Spring':
    price = 3000
elif season == 'Summer' or season == 'Autumn':
    price = 4200
elif season == 'Winter':
    price = 2600
if fishermen <= 6:
    price *= 0.9
elif 7 <= fishermen <= 11:
    price *= 0.85
elif fishermen >= 12:
    price *= 0.75
if fishermen % 2 == 0 and season != 'Autumn':
    price *= 0.95
result = budget - price
if budget >= price:
    print(f'Yes! You have {result:.2f} leva left.')
else:
    print(f'Not enough money! You need {abs(result):.2f} leva.')
# ----------------------------------------------------03. New House
flowers = input()
flowers_count = int(input())
budget = int(input())
price = 0
if flowers == 'Roses':
    price = 5
    if flowers_count > 80:
        price *= 0.9
elif flowers == 'Dahlias':
    price = 3.8
    if flowers_count > 90:
        price *= 0.85
elif flowers == 'Tulips':
    price = 2.8
    if flowers_count > 80:
        price *= 0.85
elif flowers == 'Narcissus':
    price = 3
    if flowers_count < 120:
        price *= 1.15
elif flowers == 'Gladiolus':
    price = 2.5
    if flowers_count < 80:
        price *= 1.20
full_price = price * flowers_count
result = budget - full_price
if budget >= full_price:
    print(f'Hey, you have a great garden with {flowers_count} {flowers} and {result:.2f} leva left.')
else:
    print(f'Not enough money, you need {abs(result):.2f} leva more.')
# ----------------------------------------------------02. Summer Outfit
temperature = int(input())
time = input()
if time == 'Morning':
    if 10 <= temperature <= 18:
        outfit = 'Sweatshirt'
        shoes = 'Sneakers'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
elif time == 'Afternoon':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'T-Shirt'
        shoes = 'Sandals'
    elif temperature >= 25:
        outfit = 'Swim Suit'
        shoes = 'Barefoot'
elif time == 'Evening':
    if 10 <= temperature <= 18:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif 18 < temperature <= 24:
        outfit = 'Shirt'
        shoes = 'Moccasins'
    elif temperature >= 25:
        outfit = 'Shirt'
        shoes = 'Moccasins'
print(f"It's {temperature} degrees, get your {outfit} and {shoes}.")
# ----------------------------------------------------01.Cinema
category = input()
row = int(input())
col = int(input())
result = row * col
if category == 'Premiere':
    result *= 12
elif category == 'Normal':
    result *= 7.5
elif category == 'Discount':
    result *= 5
print(f'{result:.2f} leva')

