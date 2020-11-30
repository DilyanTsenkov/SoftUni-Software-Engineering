shops = input().split()
commands = int(input())

for i in range(commands):
    length = len(shops)
    command = input().split()

    if command[0] == "Include":
        shops.append(command[1])

    elif command[0] == "Visit":
        index = int(command[2])
        if index <= length:
            if command[1] == "first":
                shops = shops[index:]
            elif command[1] == "last":
                shops = shops[:(length - index)]

    elif command[0] == "Prefer":
        index_one = int(command[1])
        index_two = int(command[2])
        if (0 <= index_one < length) and (0 <= index_two < length):
            shops[index_one], shops[index_two] = shops[index_two], shops[index_one]

    elif command[0] == "Place":
        index = int(command[2])
        if 0 <= index < length:
            shops.insert(index + 1, command[1])

print("Shops left:")
print(" ".join(shops))
