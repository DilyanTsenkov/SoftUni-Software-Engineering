first_char = input()
second_char = input()
string = input()

char_sum = 0

for char in string:
    if ord(first_char) < ord(char) < ord(second_char):
        char_sum += ord(char)

print(char_sum)
