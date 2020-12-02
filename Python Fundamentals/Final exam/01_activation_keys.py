def contains(r_key, com):
    substring = com[1]
    if substring in r_key:
        print(f"{r_key} contains {substring}")
    else:
        print("Substring not found!")
    return r_key


def flip(r_key, com):
    upper_lower = com[1]
    start_index = int(com[2])
    end_index = int(com[3])
    part_key = r_key[start_index:end_index]
    if upper_lower == "Upper":
        part_key = part_key.upper()
    else:
        part_key = part_key.lower()
    r_key = r_key[:start_index] + part_key + r_key[end_index:]
    print(r_key)
    return r_key


def slice(r_key, com):
    start_index = int(com[1])
    end_index = int(com[2])
    r_key = r_key[:start_index] + r_key[end_index:]
    print(r_key)
    return r_key


raw_key = input()

while True:
    command = input()
    if command == "Generate":
        break
    command = command.split(">>>")
    action = command[0]

    if action == "Contains":
        raw_key = contains(raw_key, command)
    elif action == "Flip":
        raw_key = flip(raw_key, command)
    elif action == "Slice":
        raw_key = slice(raw_key, command)

print(f"Your activation key is: {raw_key}")
