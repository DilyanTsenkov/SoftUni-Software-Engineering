targets = input().split("|")
targets = [int(target) for target in targets]

points = 0

while True:
    command = input().split("@")

    if command[0] == "Game over":
        break

    elif command[0][0] == "S" and int(command[1]) in range(len(targets)):
        if command[0] == "Shoot Left":
            index = (int(command[1]) - int(command[2])) % len(targets)
        elif command[0] == "Shoot Right":
            index = (int(command[1]) + int(command[2])) % len(targets)

        if targets[index] < 5:
            points += targets[index]
            targets[index] = 0
        else:
            points += 5
            targets[index] -= 5

    elif command[0] == "Reverse":
        targets.reverse()

targets = [str(target) for target in targets]

print(" - ".join(targets))
print(f"Iskren finished the archery tournament with {points} points!")

