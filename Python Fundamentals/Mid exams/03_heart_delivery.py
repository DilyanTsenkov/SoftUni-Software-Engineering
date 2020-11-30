neighborhood = list(map(int, (input().split("@"))))

index = 0

while True:
    command = input().split()
    action = command[0]

    if action == "Love!":
        break
    length = int(command[1])

    if action == "Jump":
        index += length
        if index not in range(len(neighborhood)):
            index = 0
        if neighborhood[index] > 0:
            neighborhood[index] -= 2
            if neighborhood[index] == 0:
                print(f"Place {index} has Valentine's day.")
        else:
            print(f"Place {index} already had Valentine's day.")

print(f"Cupid's last position was {index}.")

neighborhood = [house for house in neighborhood if house != 0]

if len(neighborhood) == 0:
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighborhood)} places.")
