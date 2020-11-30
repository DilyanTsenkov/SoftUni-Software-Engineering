first_line = input().split(" ")
second_line = input().split(" ")
third_line = input().split(" ")

wining_player = ""

for i in range(3):
    if first_line[i] == second_line[i] == third_line[i]:
        wining_player = first_line[i]
        break

for i in range(1):
    if first_line[i] == first_line[i + 1] == first_line[i + 1]:
        wining_player = first_line[i]
        break
    elif second_line[i] == second_line[i + 1] == second_line[i + 1]:
        wining_player = second_line[i]
        break
    elif third_line[i] == third_line[i + 1] == third_line[i + 1]:
        wining_player = third_line[i]
        break

if first_line[0] == second_line[1] == third_line[2]:
    wining_player = first_line[0]
if first_line[2] == second_line[1] == third_line[0]:
    wining_player = third_line[0]

if wining_player == "1":
    print("First player won")
elif wining_player == "2":
    print("Second player won")
else:
    print("Draw!")
