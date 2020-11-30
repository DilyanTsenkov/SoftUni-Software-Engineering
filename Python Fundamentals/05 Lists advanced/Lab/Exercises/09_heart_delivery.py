neighborhood = input().split("@")
neighborhood = [int(element) for element in neighborhood]

command = input().split()

jump = 0
position = 0

while command[0] != "Love!":
    jump += int(command[1])
    if jump >= len(neighborhood):
        jump = 0

    for i in range(len(neighborhood)):
        if jump == i:
            if neighborhood[i] <= 0:
                print(f"Place {i} already had Valentine's day.")
            else:
                neighborhood[i] -= 2
                if neighborhood[i] <= 0:
                    print(f"Place {i} has Valentine's day.")
            position = i
            break
    command = input().split()

print(f"Cupid's last position was {position}.")

if sum(neighborhood) == 0:
    print("Mission was successful.")
else:
    neighborhood = [el for el in neighborhood if el != 0]
    print(f"Cupid has failed {len(neighborhood)} places.")