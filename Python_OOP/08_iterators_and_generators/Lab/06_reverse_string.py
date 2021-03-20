def reverse_text(string):
    for char in range(len(string) - 1, -1, -1):
        yield string[char]


for char in reverse_text("step"):
    print(char, end='')
