import math

days = int(input())
food_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_g = float(input())
needed_food = days * dog_food_kg + days * cat_food_kg + days * turtle_food_g / 1000
result = food_kg - needed_food
if food_kg >= needed_food:
    print(f'{math.floor(result)} kilos of food left.')
else:
    print(f'{math.ceil(abs(result))} more kilos of food are needed.')
