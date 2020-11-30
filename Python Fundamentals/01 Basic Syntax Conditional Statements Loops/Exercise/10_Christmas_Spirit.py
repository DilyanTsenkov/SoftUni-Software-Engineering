quantity = int(input())
days = int(input())

ornament_set = 2
tree_skirt = 5
tree_garlands = 3
tree_lights = 15
christmas_spirit = 0
costs = 0
counter = 0

for day in range(1, days + 1):
    counter += 1
    if counter == 11:
        quantity += 2
        counter = 0
    if day % 2 == 0:
        costs += (ornament_set * quantity)
        christmas_spirit += 5
    if day % 3 == 0:
        costs += (tree_skirt * quantity + tree_garlands * quantity)
        christmas_spirit += 13
    if day % 5 == 0:
        costs += (tree_lights * quantity)
        christmas_spirit += 17
        if day % 3 == 0:
            christmas_spirit += 30
    if day % 10 == 0:
        christmas_spirit -= 20
        costs += (tree_skirt + tree_garlands + tree_lights)
        if day == days:
            christmas_spirit -= 30

print(f"Total cost: {costs}")
print(f"Total spirit: {christmas_spirit}")
