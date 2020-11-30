#-----------------------------------------------------------------06. Honey Winter Reserves
honey_for_winter = float(input())
total_honey = 0
while True:
    bee_name = input()
    if bee_name == "Winter has come":
        if total_honey >= honey_for_winter:
            print(f"Well done! Honey surplus {difference:.2f}.")
        else:
            print(f"Hard Winter! Honey needed {difference:.2f}.")
        break
    bee_honey = 0
    for bee in range(6):
        honey = float(input())
        if honey < 0:
            bee_honey -= abs(honey)
        else:
            bee_honey += honey
    if bee_honey < 0:
        print(f"{bee_name} was banished for gluttony")
    total_honey += bee_honey
    difference = abs(total_honey - honey_for_winter)
    if total_honey >= honey_for_winter:
        print(f"Well done! Honey surplus {difference:.2f}.")
        break
#-----------------------------------------------------------------05. Beehive Defense
bees = int(input())
health = int(input())
attack = int(input())
while True:
    bees -= attack
    health = health - bees * 5
    if health <= 0:
        print(f"Beehive won! Bees left {bees}.")
        break
    if bees < 100:
        if bees < 0:
            print(f"The bear stole the honey! Bees left {0}.")
        else:
            print(f"The bear stole the honey! Bees left {bees}.")
        break
#-----------------------------------------------------------------04. Beehive Population
import math
start_population = int(input())
years = int(input())
bees = 0
population = start_population
for year in range(1, years + 1):
    bees = math.floor(population / 10)
    population = population + bees * 2
    if year % 5 == 0:
        bees = math.floor(population / 50)
        population = population - bees * 5
    bees = math.floor(population / 20)
    population = population - bees * 2
print(f"Beehive population: {population}")
#-----------------------------------------------------------------03. Honey Harvest
flower = input()
flowers_count = int(input())
season = input()
honey = 0
if season == "Spring":
    if flower == "Daisy":
        honey = 12 * 1.1
    elif flower == "Mint":
        honey = 10 * 1.1
    elif flower == "Lavender":
        honey = 12
    else:
        honey = 10
elif season == "Summer":
    if flower == "Mint":
        honey = 12
    else:
        honey = 8
else:
    if flower == "Sunflower":
        honey = 12
    else:
        honey = 6
total_honey = flowers_count * honey
if season == "Summer":
    total_honey *= 1.1
elif season == "Autumn":
    total_honey *= 0.95
print(f"Total honey harvested: {total_honey:.2f}")
#-----------------------------------------------------------------02. Beehive Role
intellect = int(input())
power = int(input())
sex = input()
roll = ""
if intellect >= 80 and power >= 80 and sex == "female":
    roll = "Queen Bee"
elif intellect >= 80:
    roll = "Repairing Bee"
elif intellect >= 60:
    roll = "Cleaning Bee"
elif power >= 80 and sex == "male":
    roll = "Drone Bee"
elif power >= 60:
    roll = "Guard Bee"
else:
    roll = "Worker Bee"
print(roll)
#-----------------------------------------------------------------01. Honeycombs
bees = int(input())
flowers = int(input())
honey = bees * flowers * 0.21
honeycombs = honey // 100
honeycombs_left = honey % 100
print(f"{int(honeycombs)} honeycombs filled.")
print(f"{honeycombs_left:.2f} grams of honey left.")
