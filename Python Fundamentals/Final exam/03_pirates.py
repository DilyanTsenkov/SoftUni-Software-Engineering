places = {}

while True:
    target = input()
    if target == "Sail":
        break

    city, population, gold = target.split("||")
    population = int(population)
    gold = int(gold)

    if city not in places:
        places[city] = [population, gold]
    else:
        if city in places:
            places[city][0] += population
            places[city][1] += gold

while True:
    events = input()
    if events == "End":
        break

    events = events.split("=>")
    event = events[0]
    town = events[1]

    if event == "Plunder":
        people = int(events[2])
        gold = int(events[3])
        print(f"{town} plundered! {gold} gold stolen, {people} citizens killed.")
        places[town][1] -= gold
        places[town][0] -= people
        if places[town][0] == 0 or places[town][1] == 0:
            removed_town = places.pop(town)
            print(f"{town} has been wiped off the map!")
    elif event == "Prosper":
        gold = int(events[2])
        if gold < 0:
            print("Gold added cannot be a negative number!")
        else:
            places[town][1] += gold
            print(f"{gold} gold added to the city treasury. {town} now has {places[town][1]} gold.")

places = dict(sorted(places.items(), key=lambda x: (-x[1][1], x[0])))

if places:
    print(f"Ahoy, Captain! There are {len(places)} wealthy settlements to go to:")
    for key, value in places.items():
        print(f"{key} -> Population: {value[0]} citizens, Gold: {value[1]} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
