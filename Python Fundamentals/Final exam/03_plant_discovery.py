def plants(number):
    my_plants = {}
    for num in range(number):
        plant, rarity = input().split("<->")
        my_plants[plant] = {"Rarity": int(rarity), "Rating": []}

    return my_plants


number = int(input())
my_plants = plants(number)

while True:
    commands = input()
    if commands == "Exhibition":
        break
    commands = commands.split(": ")
    action = commands.pop(0)
    temp = commands[0].split(" - ")
    plant = temp[0]
    if plant not in my_plants:
        print("error")
    else:
        if action == "Rate":
            rating = int(temp[1])
            my_plants[plant]["Rating"].append(rating)
        elif action == "Update":
            new_rarity = int(temp[1])
            my_plants[plant]["Rarity"] = new_rarity
        elif action == "Reset":
            my_plants[plant]["Rating"] = []

for rate in my_plants.values():
    if len(rate["Rating"]) > 0:
        rate["Rating"] = (sum(rate["Rating"]) / len(rate["Rating"]))
    else:
        rate["Rating"] = 0

my_plants = dict(sorted(my_plants.items(), key=lambda x: (-x[1]["Rarity"], -x[1]["Rating"])))
print('Plants for the exhibition:')
for key, value in my_plants.items():
    print(f'- {key}; Rarity: {my_plants[key]["Rarity"]}; Rating: {my_plants[key]["Rating"]:.2f}')
