def cheat():
    add_element = f"-{moves}a"
    add_index = len(elements) // 2
    elements.insert(add_index, add_element)
    elements.insert(add_index, add_element)
    print("Invalid input! Adding additional elements to the board")
    return elements


def matching(i1, i2):
    match = elements[first_index]
    index_to_remove = [first_index, second_index]
    for i in sorted(index_to_remove, reverse=True):
        del elements[i]
    print(f"Congrats! You have found matching elements - {match}!")
    return elements


elements = input().split()
moves = 0

while True:
    indexes = input()

    if indexes == "end":
        print("Sorry you lose :(")
        print(" ".join(elements))
        break

    indexes = indexes.split()
    first_index = int(indexes[0])
    second_index = int(indexes[1])
    moves += 1

    if first_index == second_index or first_index not in range(len(elements)) or second_index not in range(
            len(elements)):
        elements = cheat()

    elif elements[first_index] == elements[second_index]:
        elements = matching(first_index, second_index)

    elif elements[first_index] != elements[second_index]:
        print("Try again!")

    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        break
