days = int(input())
hours = int(input())
all_days_parking = 0
for day in range(1, days + 1):
    parking_price_per_day = 0
    for hour in range(1, hours + 1):
        if day % 2 == 0 and hour % 2 == 1:
            price = 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            price = 1.25
        else:
            price = 1
        parking_price_per_day += price
    print(f"Day: {day} - {parking_price_per_day:.2f} leva")
    all_days_parking += parking_price_per_day
print(f"Total: {all_days_parking:.2f} leva")
# -----------------------------------------------------------------------05. Division Without Remainder
n = int(input())
counter_2 = 0
counter_3 = 0
counter_4 = 0
for number in range(0, n):
    input_number = int(input())
    if input_number % 2 == 0:
        counter_2 += 1
    if input_number % 3 == 0:
        counter_3 += 1
    if input_number % 4 == 0:
        counter_4 += 1
percent_2 = counter_2 / n * 100
percent_3 = counter_3 / n * 100
percent_4 = counter_4 / n * 100
print(f"{percent_2:.2f}%\n{percent_3:.2f}%\n{percent_4:.2f}%")
# -----------------------------------------------------------------------04. Tourist Shop
budget = float(input())
purchase_price = 0
purchase_counter = 0
product = input()
while product != "Stop":
    product_price = float(input())
    purchase_counter += 1
    if purchase_counter % 3 == 0:
        product_price = product_price / 2
    purchase_price += product_price
    if purchase_price > budget:
        break
    product = input()
difference = purchase_price - budget
if product == "Stop":
    print(f"You bought {purchase_counter} products for {purchase_price:.2f} leva.")
else:
    print(f"You don't have enough money!\nYou need {difference:.2f} leva!")
# ----------------------------------------------------------------------03. Mobile operator
contract_duration = input()
contract_type = input()
mobile_internet = input()
months_to_pay = int(input())
mobile_internet_price = 0
if contract_type == "Small":
    if contract_duration == "one":
        monthly_price = 9.98
    else:
        monthly_price = 8.58
elif contract_type == "Middle":
    if contract_duration == "one":
        monthly_price = 18.99
    else:
        monthly_price = 17.09
elif contract_type == "Large":
    if contract_duration == "one":
        monthly_price = 25.98
    else:
        monthly_price = 23.59
else:
    if contract_duration == "one":
        monthly_price = 35.99
    else:
        monthly_price = 31.79
if mobile_internet == "yes":
    if monthly_price <= 10:
        mobile_internet_price = 5.50
    elif 10 < monthly_price <= 30:
        mobile_internet_price = 4.35
    else:
        mobile_internet_price = 3.85
total_price = months_to_pay * (monthly_price + mobile_internet_price)
if contract_duration == "two":
    total_price = total_price * 0.9625
print(f"{total_price:.2f} lv.")
# ----------------------------------------------------------------------02. Safari
budget = float(input())
fuel = float(input())
day = input()
if day == "Saturday":
    excursion_price = 0.9 * (fuel * 2.1 + 100)
else:
    excursion_price = 0.8 * (fuel * 2.1 + 100)
result = abs(budget - excursion_price)
if budget >= excursion_price:
    print(f"Safari time! Money left: {result:.2f} lv. ")
else:
    print(f"Not enough money! Money needed: {result:.2f} lv.")
# ----------------------------------------------------------------------01. Food Delivery
chicken_menu = int(input())
fish_menu = int(input())
vegetarian_menu = int(input())
food = chicken_menu * 10.35 + fish_menu * 12.40 + vegetarian_menu * 8.15
desert = food * 0.2
total = food + desert + 2.5
print(f"Total: {total:.2f}")