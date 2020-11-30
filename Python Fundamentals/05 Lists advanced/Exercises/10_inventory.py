items = input().split(", ")
command = input().split(" - ")

while command[0] != "Craft!":
    item = command[1]
    action = command[0]

    if action == "Collect":
        if item not in items:
            items.append(item)
    elif action == "Drop":
        if item in items:
            items.remove(item)
    elif action == "Combine Items":
        item = item.split(":")
        if item[0] in items:
            insert_index = items.index(item[0]) + 1
            items.insert(insert_index, item[1])
    elif action == "Renew":
        if item in items:
            item_to_move = items.pop(items.index(item))
            items.append(item_to_move)

    command = input().split(" - ")

print(", ".join(items))