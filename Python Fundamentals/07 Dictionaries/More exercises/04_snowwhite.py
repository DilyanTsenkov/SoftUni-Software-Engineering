from collections import Counter


def add_dwarf(dwarfs, counter, dwarf_name, dwarf_color, dwarf_physics):
    if not dwarfs:
        counter += 1
        dwarfs[counter] = {"name": dwarf_name, "hat": dwarf_color, "physics": dwarf_physics}
    else:
        found = False
        for key in dwarfs.keys():
            if dwarfs[key]["name"] == dwarf_name and dwarfs[key]["hat"] == dwarf_color:
                dwarfs[key]["physics"] = max(dwarfs[key]["physics"], dwarf_physics)
                found = True
                break
        if not found:
            counter += 1
            dwarfs[counter] = {"name": dwarf_name, "hat": dwarf_color, "physics": dwarf_physics}
    return dwarfs, counter


counter = 0
dwarfs = {}

while True:
    receive = input()
    if receive == "Once upon a time":
        break
    dwarf_name, dwarf_color, dwarf_physics = receive.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    dwarfs, counter = add_dwarf(dwarfs, counter, dwarf_name, dwarf_color, dwarf_physics)

counts = Counter([list(d.values())[1] for d in dwarfs.values()])
sorted_dwarfs = dict(sorted(dwarfs.items(), key=lambda x: (-x[1]["physics"], -counts[x[1]["hat"]])))

for value in sorted_dwarfs.values():
    print(f'({value["hat"]}) {value["name"]} <-> {value["physics"]}')
