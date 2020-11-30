key = int(input())
n_characters = int(input())

result = ""

for char in range(n_characters):
    character = input()
    key_character = chr(ord(character) + key)
    result += key_character

print(result)
