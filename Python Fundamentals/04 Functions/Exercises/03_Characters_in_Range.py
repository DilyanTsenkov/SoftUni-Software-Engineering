def char_range(start, end):
    result = []
    for char in range(ord(start) + 1, ord(end)):
        result.append(chr(char))
    return " ".join(result)


first_char = input()
second_char = input()

print(char_range(first_char, second_char))
