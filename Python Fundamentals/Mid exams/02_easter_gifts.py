name_of_gifts = input().split()

while True:
    command = input().split()
    if " ".join(command) == "No Money":
        break

    elif command[0] == "OutOfStock":
        if command[1] in name_of_gifts:
            for i in range(len(name_of_gifts)):
                if name_of_gifts[i] == command[1]:
                    name_of_gifts[i] = None

    elif command[0] == "Required":
        if 0 <= int(command[2]) < len(name_of_gifts):
            name_of_gifts[int(command[2])] = command[1]

    elif command[0] == "JustInCase":
        name_of_gifts[-1] = command[1]

name_of_gifts = [gift for gift in name_of_gifts if gift != None]

print(" ".join(name_of_gifts))
