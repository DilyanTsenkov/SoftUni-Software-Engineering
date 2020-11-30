targets = list(map(int, input().split()))


def shoot(i, v):
    if i in range(len(targets)):
        targets[i] -= v
        if targets[i] <= 0:
            targets.pop(i)
            return targets
    return targets


def add(i, v):
    if i in range(len(targets)):
        targets.insert(i, v)
    else:
        print("Invalid placement!")
    return targets


def strike(i, v):
    start_index = i - v
    end_index = i + v + 1
    if start_index >= 0 and end_index in range(len(targets)):
        targets_removed = targets[:start_index] + targets[end_index:]
        return targets_removed
    else:
        print("Strike missed!")
        return targets


while True:
    command = input().split()
    if command[0] == "End":
        break
    action = command[0]
    index = int(command[1])
    value = int(command[2])

    if action == "Shoot":
        targets = shoot(index, value)

    elif action == "Add":
        targets = add(index, value)

    elif action == "Strike":
        targets = strike(index, value)

targets = [str(target) for target in targets]

print("|".join(targets))
