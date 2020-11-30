words = input().split()

while True:
    command = input().split()
    if command[0] == "Stop":
        break
    elif command[0] == "Delete":
        if int(command[1]) + 1 < len(words):
            words.pop(int(command[1]) + 1)
    elif command[0] == "Swap":
        if command[1] in words and command[2] in words:
            first_word_index = words.index(command[1])
            second_word_index = words.index(command[2])
            words[first_word_index] = command[2]
            words[second_word_index] = command[1]
    elif command[0] == "Put":
        if 0 <= int(command[2]) - 1 <= len(words):
            words.insert(int(command[2]) - 1, command[1])
    elif command[0] == "Sort":
        words.sort(reverse=True)
    elif command[0] == "Replace":
        if command[2] in words:
            second_word_index = words.index(command[2])
            words[second_word_index] = command[1]

print(" ".join(words))
