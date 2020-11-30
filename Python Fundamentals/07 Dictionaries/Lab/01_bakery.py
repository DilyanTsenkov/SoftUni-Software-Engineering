food_quantities = input().split()

bakery = {}

for i in range(0, len(food_quantities), 2):
    food = food_quantities[i]
    quantity = food_quantities[i + 1]
    bakery[food] = int(quantity)

print(bakery)
