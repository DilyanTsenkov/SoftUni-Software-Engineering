# ---------------------------------------13. Ski Trip
days = int(input())
stay_in = input()
rating = input()
room = 18
apartment = 25
president_apartment = 35
holiday = room * (days - 1)
if days < 10:
    if stay_in == 'apartment':
        holiday = apartment * (days - 1) * 0.7
    elif stay_in == 'president apartment':
        holiday = president_apartment * (days - 1) * 0.9
elif 10 <= days <= 15:
    if stay_in == 'apartment':
        holiday = apartment * (days - 1) * 0.65
    elif stay_in == 'president apartment':
        holiday = president_apartment * (days - 1) * 0.75
elif days > 15:
    if stay_in == 'apartment':
        holiday = apartment * (days - 1) * 0.5
    elif stay_in == 'president apartment':
        holiday = president_apartment * (days - 1) * 0.8
if rating == 'positive':
    holiday += holiday * 0.25
else:
    holiday -= holiday * 0.1
print(f'{holiday:.2f}')
# ---------------------------------------12. Trade Commissions
city = input()
sold_out = float(input())
commission = 0
if city == 'Sofia':
    if 0 <= sold_out <= 500:
        commission = sold_out * 0.05
    elif 500 <= sold_out <= 1000:
        commission = sold_out * 0.07
    elif 1000 <= sold_out <= 10000:
        commission = sold_out * 0.08
    elif sold_out > 10000:
        commission = sold_out * 0.12
elif city == 'Varna':
    if 0 <= sold_out <= 500:
        commission = sold_out * 0.045
    elif 500 <= sold_out <= 1000:
        commission = sold_out * 0.075
    elif 1000 <= sold_out <= 10000:
        commission = sold_out * 0.10
    elif sold_out > 10000:
        commission = sold_out * 0.13
elif city == 'Plovdiv':
    if 0 <= sold_out <= 500:
        commission = sold_out * 0.055
    elif 500 <= sold_out <= 1000:
        commission = sold_out * 0.08
    elif 1000 <= sold_out <= 10000:
        commission = sold_out * 0.12
    elif sold_out > 10000:
        commission = sold_out * 0.145
if commission > 0:
    print(f'{commission:.2f}')
else:
    print('error')
# ---------------------------------------11. Fruit Shop
fruit = input()
day = input()
quantity = float(input())
price = 0
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    if fruit == 'banana':
        price = 2.50
    elif fruit == 'apple':
        price = 1.20
    elif fruit == 'orange':
        price = 0.85
    elif fruit == 'grapefruit':
        price = 1.45
    elif fruit == 'kiwi':
        price = 2.70
    elif fruit == 'pineapple':
        price = 5.50
    elif fruit == 'grapes':
        price = 3.85
elif day == 'Saturday' or day == 'Sunday':
    if fruit == 'banana':
        price = 2.70
    elif fruit == 'apple':
        price = 1.25
    elif fruit == 'orange':
        price = 0.9
    elif fruit == 'grapefruit':
        price = 1.60
    elif fruit == 'kiwi':
        price = 3.00
    elif fruit == 'pineapple':
        price = 5.60
    elif fruit == 'grapes':
        price = 4.20
shopping = quantity * price
if shopping > 0:
    print(f'{shopping:.2f}')
else:
    print('error')
# ---------------------------------------10. Invalid Number
number = int(input())
if (number != 0 and number < 100) or (number != 0 and number > 200):
    print('invalid')
# ---------------------------------------09. Fruit or Vegetable
product = input()
if product == 'banana' or product == 'apple' or product == 'kiwi' or product == 'cherry' or product == 'lemon' or product == 'grapes':
    print('fruit')
elif product == 'tomato' or product == 'cucumber' or product == 'pepper' or product == 'carrot':
    print('vegetable')
else:
    print('unknown')
# ---------------------------------------08.Cinema Ticket
day = input()
if day == 'Wednesday' or day == 'Thursday':
    ticket = 14
elif day == 'Saturday' or day == 'Sunday':
    ticket = 16
else:
    ticket = 12
print(ticket)
# ---------------------------------------07.Working Hours
hour = int(input())
day = input()
if 10 <= hour <= 18 and (
        day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday' or day == 'Saturday'):
    print('open')
else:
    print('closed')
# ---------------------------------------06. Number in Range
number = int(input())
if -100 <= number <= 100 and number != 0:
    print('Yes')
else:
    print('No')
# ---------------------------------------05. Small Shop
product = input()
city = input()
quantity = float(input())
if city == 'Sofia':
    if product == 'coffee':
        price = 0.5
    elif product == 'water':
        price = 0.8
    elif product == 'beer':
        price = 1.20
    elif product == 'sweets':
        price = 1.45
    elif product == 'peanuts':
        price = 1.60
elif city == 'Plovdiv':
    if product == 'coffee':
        price = 0.4
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.15
    elif product == 'sweets':
        price = 1.30
    elif product == 'peanuts':
        price = 1.50
elif city == 'Varna':
    if product == 'coffee':
        price = 0.45
    elif product == 'water':
        price = 0.7
    elif product == 'beer':
        price = 1.10
    elif product == 'sweets':
        price = 1.35
    elif product == 'peanuts':
        price = 1.55
full_price = price * quantity
print(full_price)
# ---------------------------------------04. Personal Titles
age = float(input())
sex = input()
output = ''
if age >= 16:
    if sex == 'm':
        output = 'Mr.'
    elif sex == 'f':
        output = 'Ms.'
elif age < 16:
    if sex == 'm':
        output = 'Master'
    elif sex == 'f':
        output = 'Miss'
print(output)
# ---------------------------------------03. Animal Type
animal = input()
if animal == 'dog':
    print('mammal')
elif animal == 'crocodile' or animal == 'tortoise' or animal == 'snake':
    print('reptile')
else:
    print('unknown')
# ---------------------------------------02.Weekend or Working Day
day = input()
if day == 'Monday' or day == 'Tuesday' or day == 'Wednesday' or day == 'Thursday' or day == 'Friday':
    print('Working day')
elif day == 'Saturday' or day == 'Sunday':
    print('Weekend')
else:
    print('Error')
# ---------------------------------------01. Day of Week
number = int(input())
if number == 1:
    day = 'Monday'
elif number == 2:
    day = 'Tuesday'
elif number == 3:
    day = 'Wednesday'
elif number == 4:
    day = 'Thursday'
elif number == 5:
    day = 'Friday'
elif number == 6:
    day = 'Saturday'
elif number == 7:
    day = 'Sunday'
else:
    day = 'Error'
print(day)
