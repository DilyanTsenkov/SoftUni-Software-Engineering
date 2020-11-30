# ----------------------------------------------------------------06. Tournament of Christmas
tournament_days = int(input())
charity = 0
day_win_counter = 0
for day in range(tournament_days):
    day_charity = 0
    win_counter = 0
    lose_counter = 0
    sport = input()
    while sport != "Finish":
        result = input()
        if result == "win":
            day_charity += 20
            win_counter += 1
        else:
            lose_counter += 1
        sport = input()
    if win_counter > lose_counter:
        day_charity *= 1.1
        day_win_counter += 1
        charity += day_charity
    else:
        charity += day_charity
if day_win_counter > tournament_days / 2:
    charity *= 1.2
    print(f"You won the tournament! Total raised money: {charity:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {charity:.2f}")
# ----------------------------------------------------------------05. Suitcases Load
capacity = float(input())
luggage_counter = 0
while True:
    luggage = input()
    if luggage == "End":
        print("Congratulations! All suitcases are loaded!")
        break
    luggage_counter += 1
    if luggage_counter != 0 and luggage_counter % 3 == 0:
        capacity = capacity - float(luggage) * 1.1
    else:
        capacity -= float(luggage)
    if capacity < 0:
        print("No more space!")
        luggage_counter -= 1
        break
print(f"Statistic: {luggage_counter} suitcases loaded.")
# ----------------------------------------------------------------05. Care of Puppy
food_kg = int(input())
food_in_grams = 0
food_g = input()
while food_g != "Adopted":
    food_in_grams += int(food_g)
    food_g = input()
result = abs(food_in_grams - food_kg * 1000)
if food_in_grams / 1000 <= food_kg:
    print(f"Food is enough! Leftovers: {result} grams.")
else:
    print(f"Food is not enough. You need {result} grams more.")
# -----------------------------------------------------------------04. Trekking Mania
groups = int(input())
musala = 0
monblan = 0
kilimandjaro = 0
k2 = 0
everst = 0
climbers_counter = 0
for group in range(groups):
    climbers = int(input())
    if climbers <= 5:
        musala += climbers
    elif 5 < climbers <= 12:
        monblan += climbers
    elif 12 < climbers <= 25:
        kilimandjaro += climbers
    elif 25 < climbers <= 40:
        k2 += climbers
    elif 40 <= climbers:
        everst += climbers
    climbers_counter += climbers
musala_percent = musala / climbers_counter * 100
monblan_percent = monblan / climbers_counter * 100
kilimandjaro_percent = kilimandjaro / climbers_counter * 100
k2_percent = k2 / climbers_counter * 100
everst_percent = everst / climbers_counter * 100
print(f"{musala_percent:.2f}%")
print(f"{monblan_percent:.2f}%")
print(f"{kilimandjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everst_percent:.2f}%")
# ----------------------------------------------------------------04. Food for Pets
days = int(input())
total_food = float(input())
counter = 0
biscuit = 0
dog_food_total = 0
cat_food_total = 0
for day in range(1, days + 1):
    dog_food = int(input())
    cat_food = int(input())
    counter += 1
    if counter == 3:
        biscuit += (cat_food + dog_food) * 0.1
        counter = 0
    dog_food_total += dog_food
    cat_food_total += cat_food
percent_eaten_food = (dog_food_total + cat_food_total) * 100 / total_food
eaten_food = total_food * percent_eaten_food / 100
percent_dog_food = dog_food_total * 100 / eaten_food
percent_cat_food = cat_food_total * 100 / eaten_food
print(f"Total eaten biscuits: {biscuit:.0f}gr.")
print(f"{percent_eaten_food:.2f}% of the food has been eaten.")
print(f"{percent_dog_food:.2f}% eaten from the dog.")
print(f"{percent_cat_food:.2f}% eaten from the cat.")
# -----------------------------------------------------------------03. Fitness Card
budget = float(input())
sex = input()
age = int(input())
sport = input()
price = 0
if sex == "m":
    if sport == "Gym":
        price = 42
    elif sport == "Boxing":
        price = 41
    elif sport == "Yoga":
        price = 45
    elif sport == "Zumba":
        price = 34
    elif sport == "Dances":
        price = 51
    elif sport == "Pilates":
        price = 39
else:
    if sport == "Gym":
        price = 35
    elif sport == "Boxing":
        price = 37
    elif sport == "Yoga":
        price = 42
    elif sport == "Zumba":
        price = 31
    elif sport == "Dances":
        price = 53
    elif sport == "Pilates":
        price = 37
if age <= 19:
    price *= 0.8
if budget >= price:
    print(f"You purchased a 1 month pass for {sport}.")
else:
    print(f"You don't have enough money! You need ${abs(budget - price):.2f} more.")
# ----------------------------------------------------------------03. Energy Booster
fruit = input()
size = input()
count = int(input())
price = 0
if size == "big":
    if fruit == "Watermelon":
        price = 5 * 28.70
    elif fruit == "Mango":
        price = 5 * 19.60
    elif fruit == "Pineapple":
        price = 5 * 24.80
    else:
        price = 5 * 15.20
else:
    if fruit == "Watermelon":
        price = 2 * 56
    elif fruit == "Mango":
        price = 2 * 36.66
    elif fruit == "Pineapple":
        price = 2 * 42.10
    else:
        price = 2 * 20
result = count * price
if 400 <= result <= 1000:
    result = 0.85 * result
elif result > 1000:
    result = 0.5 * result
print(f"{result:.2f} lv.")
# ----------------------------------------------------------------02. Cat Walking
minutes_per_day = int(input())
walking_count = int(input())
calories = int(input())
burned_calories = walking_count * (minutes_per_day * 5)
if burned_calories >= calories / 2:
    print(f"Yes, the walk for your cat is enough. Burned calories per day: {burned_calories}.")
else:
    print(f"No, the walk for your cat is not enough. Burned calories per day: {burned_calories}.")
# -----------------------------------------------------------------02. Mountain Run
import math

record_in_seconds = float(input())
meters = float(input())
seconds_per_meter = float(input())
slow_down = math.floor(meters / 50) * 30
needed_seconds = meters * seconds_per_meter + slow_down
result = abs(record_in_seconds - needed_seconds)
if needed_seconds >= record_in_seconds:
    print(f"No! He was {result:.2f} seconds slower.")
else:
    print(f"Yes! The new record is {needed_seconds:.2f} seconds.")
# -----------------------------------------------------------------01. Supplies for School
pens = int(input())
markers = int(input())
liters = float(input())
discount = int(input())
needed_money = (pens * 5.8 + markers * 7.20 + liters * 1.20) * (1 - discount / 100)
print(f"{needed_money:.3f}")
# -----------------------------------------------------------------01. Change Bureau
bitcoin = int(input())
yuan = float(input())
commission = float(input())
bitcoin_euro = bitcoin * 1168 / 1.95
yuan_euro = yuan * 0.15 * 1.76 / 1.95
result = (bitcoin_euro + yuan_euro) - ((bitcoin_euro + yuan_euro) * commission/100)
print(f"{result:.2f}")
