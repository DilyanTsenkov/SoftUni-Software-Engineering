text = input()

for letter in text:
    letter = chr(ord(letter) + 3)
    print(letter, end="")
