target_sequence = input().split()
target_sequence = [int(el) for el in target_sequence]

command = input().split()

while command[0] != "End":
    index = int(command[1])
    value = int(command[2])
    if (command[0]) == "Shoot":
        if 0 <= index < len(target_sequence):
            target_sequence[index] -= value
            if target_sequence[index] <= 0:
                target_sequence.pop(index)

    elif (command[0]) == "Add":
        if 0 <= index < len(target_sequence):
            target_sequence.insert(index, value)
        else:
            print("Invalid placement!")

    elif (command[0]) == "Strike":
        if index + value < len(target_sequence) and index - value >= 0:
            start_index = index - value
            end_index = index + value + 1
            target_sequence_strike = target_sequence[:start_index] + target_sequence[end_index:]
            target_sequence = target_sequence_strike
        else:
            print("Strike missed!")

    command = input().split()

target_sequence = [str(el) for el in target_sequence]
print("|".join(target_sequence))