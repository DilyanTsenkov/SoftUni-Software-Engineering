energy = int(input())

win_counter = 0

while True:
    distance = input()

    if distance == "End of battle":
        print(f"Won battles: {win_counter}. Energy left: {energy}")
        break

    elif energy - int(distance) < 0:
        print(f"Not enough energy! Game ends with {win_counter} won battles and {energy} energy")
        break

    energy -= int(distance)
    win_counter += 1

    if win_counter % 3 == 0:
        energy += win_counter
