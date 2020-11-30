def reverse_sort(act, i1, i2):
    first_index = i1
    count = i2
    second_index = first_index + count
    if act == "reverse":
        strings[first_index:second_index] = reversed(strings[first_index:second_index])
        return strings
    elif act == "sort":
        strings[first_index:second_index] = sorted(strings[first_index:second_index])
        return strings


strings = input().split()

while True:
    command = input()
    if command == "end":
        break
    command = command.split()

    if command[0] == "reverse" or command[0] == "sort":
        strings = reverse_sort(command[0], int(command[2]), int(command[4]))

    elif command[0] == "remove":
        strings = strings[int(command[1]):]

print(", ".join(strings))
