values = list(map(int, input().split()))

while True:
    command = input().split()
    action = command[0]
    if action == "swap" or action == "multiply":
        index1 = int(command[1])
        index2 = int(command[2])

    if action == "end":
        break

    elif action == "swap":
        values[index1], values[index2] = values[index2], values[index1]

    elif action == "multiply":
        index = values[index1] * values[index2]
        values.pop(index1)
        values.insert(index1, index)

    elif action == "decrease":
        values = [values[el] - 1 for el in range(len(values))]

values = [str(values[el]) for el in range(len(values))]

print(", ".join(values))
