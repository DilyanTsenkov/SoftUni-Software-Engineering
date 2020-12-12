def add(bands, band_name, members):
    members = members.split(", ")
    if band_name not in bands:
        bands[band_name] = {"members": members, "time": 0}
    else:
        members_to_add = [member for member in members if member not in bands[band_name]["members"]]
        bands[band_name]["members"].extend(members_to_add)
    return bands


def play(bands, band_name, time):
    if band_name not in bands:
        bands[band_name] = {"members": [], "time": time}
    else:
        bands[band_name]["time"] += time
    return bands


bands = {}
while True:
    command = input()
    if command == "start of concert":
        break
    command = command.split("; ")
    action = command[0]
    band_name = command[1]

    if action == "Add":
        bands = add(bands, band_name, command[2])
    elif action == "Play":
        bands = play(bands, band_name, int(command[2]))

total_time = 0
for key in bands.keys():
    total_time += bands[key]["time"]
print(f"Total time: {total_time}")

bands = dict(sorted(bands.items(), key=lambda x: (-x[1]["time"], x[0])))
for key in bands.keys():
    print(f"{key} -> {bands[key]['time']}")

band_members = input()
print(band_members)
for member in bands[band_members]["members"]:
    print(f"=> {member}")
