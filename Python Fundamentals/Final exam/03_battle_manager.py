records = {}
people = 0
while True:
    line = input()
    if line == "Results":
        break
    line = line.split(":")

    action = line[0]

    if action == "Add":
        name = line[1]
        health = int(line[2])
        energy = int(line[3])
        found = False
        for key in records.keys():
            if records[key]["name"] == name:
                found = True
                records[key]["health"] += health
        if not found:
            people += 1
            records[people] = {"name": name, "health": health, "energy": energy}

    elif action == "Attack":
        attacker = line[1]
        defender = line[2]
        damage = int(line[3])
        attacker_found = False
        defender_found = False
        for key in records.keys():
            if records[key]["name"] == attacker:
                attacker_found = True
                attacker_position = key
            if records[key]["name"] == defender:
                defender_found = True
                defender_position = key
        if attacker_found and defender_found:
            records[defender_position]["health"] -= damage
            if records[defender_position]["health"] <= 0:
                print(f"{defender_position} was disqualified!")
                records.pop(defender_position)
            records[attacker_position]["energy"] -= 1
            if records[attacker_position]["energy"] == 0:
                print(f"{attacker} was disqualified!")
                records.pop(attacker_position)
    elif action == "Delete":
        username = line[1]
        if username == "All":
            records = {}
        else:
            for key in records.keys():
                if records[key]["name"] == username:
                    records.pop(key)
                    break

print(f"People count: {len(records)}")
records = dict(sorted(records.items(), key=lambda x: (-x[1]["health"], x[1]["energy"])))
for value in records.values():
    print(f"{value['name']} - {value['health']} - {value['energy']}")
