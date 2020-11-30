# -----------------------------------------------------------------------------06. The Most Powerful Word
import math
word = input()
powerful_word = ""
powerful_word_result = 0
while word != "End of words":
    sum_of_characters = 0
    length = len(word)
    for character in word:
        sum_of_characters += ord(character)
    if word[0] == "a" or word[0] == "e" or word[0] == "i" or word[0] == "o" or word[0] == "u" or word[0] == "y" or word[
        0] == "A" or word[0] == "E" or word[0] == "I" or word[0] == "O" or word[0] == "U" or word[0] == "Y":
        sum_of_characters *= length
    else:
        sum_of_characters = math.floor(sum_of_characters / length)
    if powerful_word_result < sum_of_characters:
        powerful_word_result = sum_of_characters
        powerful_word = word
    word = input()
print(f"The most powerful word is {powerful_word} - {powerful_word_result}")
# -----------------------------------------------------------------------------06. Name Game
max_points = 0
while True:
    player_name = input()
    if player_name == "Stop":
        break
    points = 0
    for symbol in player_name:
        number = int(input())
        if number == ord(symbol):
            points += 10
        else:
            points += 2
    if max_points <= points:
        max_points = points
        player_max_points = player_name
print(f"The winner is {player_max_points} with {max_points} points!")
# -----------------------------------------------------------------------------05. Football Tournament
team = input()
games = int(input())
points = 0
wins = 0
losses = 0
draws = 0
for game in range(games):
    result = input()
    if result == "W":
        wins += 1
        points += 3
    elif result == "D":
        draws += 1
        points += 1
    elif result == "L":
        losses += 1
if games == 0:
    print(f"{team} hasn't played any games during this season.")
else:
    percent_wins = wins / games * 100
    print(f"{team} has won {points} points during this season.")
    print("Total stats:")
    print(f"## W: {wins}")
    print(f"## D: {draws}")
    print(f"## L: {losses}")
    print(f"Win rate: {percent_wins:.2f}%")
# -----------------------------------------------------------------------------05. PC Game Shop
games = int(input())
hearthstone = 0
fornite = 0
overwatch = 0
others = 0
for game in range(games):
    game_name = input()
    if game_name == "Hearthstone":
        hearthstone += 1
    elif game_name == "Fornite":
        fornite += 1
    elif game_name == "Overwatch":
        overwatch += 1
    else:
        others += 1
hearthstone_percent = hearthstone / games * 100
fornite_percent = fornite / games * 100
overwatch_percent = overwatch / games * 100
others_percent = others / games * 100
print(f"Hearthstone - {hearthstone_percent:.2f}%")
print(f"Fornite - {fornite_percent:.2f}%")
print(f"Overwatch - {overwatch_percent:.2f}%")
print((f"Others - {others_percent:.2f}%"))
# -----------------------------------------------------------------------------04. Renovation
high = int(input())
width = int(input())
percent_no_paint = int(input())
wall = high * width
room = 4 * wall - 4 * wall * (percent_no_paint / 100)
while True:
    paint = input()
    if paint == "Tired!":
        print(f"{int(room)} quadratic m left.")
        break
    room -= int(paint)
    if room < 0:
        print(f"All walls are painted and you have {abs(int(room))} l paint left!")
        break
    elif room == 0:
        print("All walls are painted! Great job, Pesho!")
        break
# -----------------------------------------------------------------------------04. Club
profit_target = float(input())
profit = 0
while True:
    cocktail_name = input()
    if cocktail_name == "Party!":
        difference = abs(profit_target - profit)
        print(f"We need {difference:.2f} leva more.")
        break
    cocktails = int(input())
    cocktail_price = len(cocktail_name)
    profit_one_order = cocktails * cocktail_price
    if profit_one_order % 2 == 1:
        profit_one_order *= 0.75
    profit += profit_one_order

    if profit >= profit_target:
        print("Target acquired.")
        break
print(f"Club income - {profit:.2f} leva.")
# -----------------------------------------------------------------------------03. Travel Agency
city = input()
holiday_type = input()
VIP = input()
days = int(input())
day_price = 0
if city == "Bansko" or "Borovets":
    if holiday_type == "withEquipment":
        day_price += 100
        if VIP == "yes":
            day_price *= 0.9
    elif holiday_type == "noEquipment":
        day_price += 80
        if VIP == "yes":
            day_price *= 0.95
if city == "Varna" or "Burgas":
    if holiday_type == "withBreakfast":
        day_price += 130
        if VIP == "yes":
            day_price *= 0.88
    elif holiday_type == "noBreakfast":
        day_price += 100
        if VIP == "yes":
            day_price *= 0.93
if days > 7:
    days -= 1
costs = day_price * days
if days < 1:
    print("Days must be positive number!")
elif ((city == "Bansko" or city == "Borovets") and (
        holiday_type == "noEquipment" or holiday_type == "withEquipment")) or (
        city == "Varna" or city == "Burgas") and (
        (holiday_type == "noBreakfast" or holiday_type == "withBreakfast")):
    print(f"The price is {costs:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
# -----------------------------------------------------------------------------03. Coffee Machine
drink = input()
sugar = input()
drinks = int(input())
price = 0
if drink == "Espresso":
    if sugar == "Without":
        price = 0.9
    elif sugar == "Normal":
        price = 1
    else:
        price = 1.20
elif drink == "Cappuccino":
    if sugar == "Without":
        price = 1
    elif sugar == "Normal":
        price = 1.2
    else:
        price = 1.6
else:
    if sugar == "Without":
        price = 0.5
    elif sugar == "Normal":
        price = 0.6
    else:
        price = 0.7
costs = drinks * price
if sugar == "Without":
    costs *= 0.65
if drink == "Espresso" and drinks >= 5:
    costs *= 0.75
if costs > 15:
    costs *= 0.8
print(f"You bought {drinks} cups of {drink} for {costs:.2f} lv.")
# -----------------------------------------------------------------------------02. Shopping
budget = float(input())
video_cards = int(input())
processors = int(input())
ram = int(input())
video_cards_price = video_cards * 250
processors_price = processors * video_cards_price * 0.35
ram_price = ram * 0.1 * video_cards_price
costs = video_cards_price + processors_price + ram_price
if video_cards > processors:
    costs *= 0.85
difference = abs(budget - costs)
if budget >= costs:
    print(f"You have {difference:.2f} leva left!")
else:
    print(f"Not enough money! You need {difference:.2f} leva more!")
# -----------------------------------------------------------------------------02. Family Trip
budget = float(input())
nights = int(input())
price_per_night = float(input())
percent_add_costs = int(input())
if nights > 7:
    price_per_night *= 0.95
costs = nights * price_per_night + (budget * percent_add_costs / 100)
difference = abs(budget - costs)
if budget >= costs:
    print(f"Ivanovi will be left with {difference:.2f} leva after vacation.")
else:
    print(f"{difference:.2f} leva needed.")
# -----------------------------------------------------------------------------01. Repainting
nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())
nylon_price = (nylon + 2) * 1.5
paint_price = paint * 1.1 * 14.50
thinner_price = thinner * 5
material_price = nylon_price + paint_price + thinner_price + 0.4
work_price = hours * material_price * 0.3
costs = material_price + work_price
print(f"Total expenses: {costs:.2f} lv.")
# -----------------------------------------------------------------------------01. Pool Day
import math

people = int(input())
entering_tax = float(input())
sunbed_tax = float(input())
umbrella_tax = float(input())
umbrellas = math.ceil(people / 2) *umbrella_tax
sunbeds = math.ceil(people * 0.75) *sunbed_tax
costs = people * entering_tax + umbrellas + sunbeds
print(f"{costs:.2f} lv.")