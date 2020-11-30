groceries = input().split("!")

while True:
    command = input().split()

    item = command[1]
    action = command[0]

    if action == "Go" and item == "Shopping!":
        break

    elif action == "Urgent":
        if item not in groceries:
            groceries.insert(0, item)

    elif action == "Unnecessary":
        if item in groceries:
            groceries.remove(item)

    elif action == "Correct":
        if item in groceries:
            index = groceries.index(item)
            groceries[index] = command[2]

    elif action == "Rearrange":
        if item in groceries:
            groceries.remove(item)
            groceries.append(item)

print(", ".join(groceries))
