# -------------------------------------------------------------06. Easter Decoration
clients = int(input())
total_spend = 0
for client in range(clients):
    counter = 0
    price = 0
    while True:
        product = input()
        if product == "Finish":
            if counter % 2 == 0:
                price *= 0.8
            print(f"You purchased {counter} items for {price:.2f} leva.")
            total_spend += price
            break
        elif product == "basket":
            price += 1.5
        elif product == "wreath":
            price += 3.8
        else:
            price += 7
        counter += 1
average = total_spend / clients
print(f"Average bill per client is: {average:.2f} leva.")
# -------------------------------------------------------------06. Easter Competition
muffins = int(input())
winning_points = 0
for muffin in range(muffins):
    backer = input()
    points = 0
    while True:
        rating = input()
        if rating == "Stop":
            print(f"{backer} has {points} points.")
            if points > winning_points:
                winner = backer
                winning_points = points
                print(f"{winner} is the new number 1!")
            break
        points += int(rating)
print(f"{winner} won competition with {winning_points} points!")
# -------------------------------------------------------------05. Easter Bake
import math

muffins = int(input())
total_sugar = 0
total_flour = 0
max_sugar = 0
max_flour = 0
for muffin in range(muffins):
    sugar = int(input())
    if sugar > max_sugar:
        max_sugar = sugar
    total_sugar += sugar
    flour = int(input())
    if flour > max_flour:
        max_flour = flour
    total_flour += flour
print(f"Sugar: {math.ceil(total_sugar / 950)}")
print(f"Flour: {math.ceil(total_flour / 750)}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")
# -------------------------------------------------------------05. Easter Eggs
painted_eggs = int(input())
red_eggs = 0
orange_eggs = 0
blue_eggs = 0
green_eggs = 0
while True:
    egg_color = input()
    if egg_color == "red":
        red_eggs += 1
    elif egg_color == "orange":
        orange_eggs += 1
    elif egg_color == "blue":
        blue_eggs += 1
    elif egg_color == "green":
        green_eggs += 1
    if painted_eggs == red_eggs+green_eggs+blue_eggs+orange_eggs:
        break
max_eggs = max(red_eggs, green_eggs, blue_eggs, orange_eggs)
if max_eggs == red_eggs:
    color = "red"
elif max_eggs == orange_eggs:
    color = "orange"
elif max_eggs == blue_eggs:
    color = "blue"
else:
    color = "green"
print(f"Red eggs: {red_eggs}")
print(f"Orange eggs: {orange_eggs}")
print(f"Blue eggs: {blue_eggs}")
print(f"Green eggs: {green_eggs}")
print(f"Max eggs: {max_eggs} -> {color}")
# -------------------------------------------------------------04. Easter Shop
egg_start = int(input())
sold_eggs = 0
while True:
    command = input()
    if command == "Close":
        print(f"Store is closed!\n{sold_eggs} eggs sold.")
        break
    eggs = int(input())
    if command == "Buy":
        sold_eggs += eggs
        if eggs > egg_start:
            print(f"Not enough eggs in store!\nYou can buy only {egg_start}.")
            break
        egg_start -= eggs
    elif command == "Fill":
        egg_start += eggs
# -------------------------------------------------------------04. Easter Eggs Battle
player_one_eggs = int(input())
player_two_eggs = int(input())
winter = input()
while winter != "End of battle":
    if winter == "one":
        player_two_eggs -= 1
    else:
        player_one_eggs -= 1
    if player_one_eggs == 0:
        print(f"Player one is out of eggs. Player two has {player_two_eggs} eggs left.")
        break
    elif player_two_eggs == 0:
        print(f"Player two is out of eggs. Player one has {player_one_eggs} eggs left.")
        break
    winter = input()
if winter == "End of battle":
    print(f"Player one has {player_one_eggs} eggs left.\nPlayer two has {player_two_eggs} eggs left.")
# -------------------------------------------------------------03. Painting Eggs
egg_size = input()
egg_color = input()
egg_lot = int(input())
price = 0
if egg_size == "Large":
    if egg_color == "Red":
        price = 16
    elif egg_color == "Green":
        price = 12
    else:
        price = 9
elif egg_size == "Medium":
    if egg_color == "Red":
        price = 13
    elif egg_color == "Green":
        price = 9
    else:
        price = 7
else:
    if egg_color == "Red":
        price = 9
    elif egg_color == "Green":
        price = 8
    else:
        price = 5
profit = egg_lot * price * 0.65
print(f"{profit:.2f} leva.")
# -------------------------------------------------------------03. Easter Trip
destination = input()
dates = input()
nights = int(input())
price = 0
if destination == "France":
    if dates == "21-23":
        price = 30
    elif dates == "24-27":
        price = 35
    else:
        price = 40
elif destination == "Italy":
    if dates == "21-23":
        price = 28
    elif dates == "24-27":
        price = 32
    else:
        price = 39
else:
    if dates == "21-23":
        price = 32
    elif dates == "24-27":
        price = 37
    else:
        price = 43
costs = nights*price
print(f"Easter trip to {destination} : {costs:.2f} leva.")
# -------------------------------------------------------------02. Easter Guests
import math

guests = int(input())
budget = int(input())
muffins = math.ceil(guests / 3) * 4
eggs = guests * 2 * 0.45
costs = muffins + eggs
difference = abs(budget - costs)
if budget >= costs:
    print(
        f"Lyubo bought {math.ceil(guests / 3)} Easter bread and {guests * 2} eggs.\nHe has {difference:.2f} lv. left.")
else:
    print(f"Lyubo doesn't have enough money.\nHe needs {difference:.2f} lv. more.")
# -------------------------------------------------------------02. Easter Party
guests = int(input())
envelope = float(input())
budget = float(input())
cake = budget * 0.1
if 10 <= guests <= 15:
    envelope *= 0.85
elif 15 < guests <= 20:
    envelope *= 0.80
elif guests > 20:
    envelope *= 0.75
costs = guests * envelope + cake
difference = abs(budget - costs)
if budget >= costs:
    print(f"It is party time! {difference:.2f} leva left.")
else:
    print(f"No party! {difference:.2f} leva needed.")
# ------------------------------------------------------------01. Easter Lunch
muffin = int(input())
eggs = int(input())
biscuits = int(input())
money_spent = muffin * 3.20 + eggs * 4.35 + biscuits * 5.4 + (0.15 * eggs * 12)
print(f"{money_spent:.2f}")
# ------------------------------------------------------------01. Easter Bakery
flour = float(input())
flour_kg = float(input())
sugar_kg = float(input())
eggs = int(input())
yeast = int(input())
costs = flour * flour_kg + (flour * 0.75 * sugar_kg) + (flour * 1.1 * eggs) + (flour * 0.75 * 0.2 * yeast)
print(f"{costs:.2f}")
