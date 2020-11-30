paintings = input().split()

while True:
    instruction = input().split()
    if instruction[0] == "END":
        break
    elif instruction[0] == "Change":
        if instruction[1] in paintings:
            index_of_first = paintings.index(instruction[1])
            paintings[index_of_first] = instruction[2]
    elif instruction[0] == "Hide":
        if instruction[1] in paintings:
            paintings = [painting for painting in paintings if painting != instruction[1]]
    elif instruction[0] == "Switch":
        if instruction[1] in paintings and instruction[2] in paintings:
            first_index = paintings.index(instruction[1])
            second_index = paintings.index(instruction[2])
            paintings[first_index], paintings[second_index] = paintings[second_index], paintings[first_index]
    elif instruction[0] == "Insert":
        if int(instruction[1]) + 1 < len(paintings):
            paintings.insert(int(instruction[1]) + 1, instruction[2])
    elif instruction[0] == "Reverse":
        paintings.reverse()

print(" ".join(paintings))
