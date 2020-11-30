legendary = {}
junk = {}
break_flag = False

while not break_flag:
    materials = input().lower().split()

    for i in range(0, len(materials), 2):
        quantity = int(materials[i])
        material = materials[i + 1]

        if material == "shards" or material == "fragments" or material == "motes":
            if material not in legendary:
                legendary[material] = quantity
            else:
                legendary[material] += quantity

            if legendary[material] >= 250:
                legendary[material] -= 250


                if material == "shards":
                    print("Shadowmourne obtained!")
                elif material == "fragments":
                    print("Valanyr obtained!")
                elif material == "motes":
                    print("Dragonwrath obtained!")

                if "fragments" not in legendary:
                    legendary["fragments"] = 0
                if "shards" not in legendary:
                    legendary["shards"] = 0
                if "motes" not in legendary:
                    legendary["motes"] = 0

                break_flag = True
                break

        else:
            if material not in junk:
                junk[material] = quantity
            else:
                junk[material] += quantity

legendary = dict(sorted(legendary.items(), key=lambda x: (-x[1], x[0])))
for material, quantity in legendary.items():
    print(f"{material}: {legendary[material]}")

junk = dict(sorted(junk.items(), key=lambda x: x[0]))

for material, quantity in junk.items():
    print(f"{material}: {junk[material]}")
