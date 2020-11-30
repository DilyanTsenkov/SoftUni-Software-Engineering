string = input()

result = []
counter = 0

for char in string:
    if 65 <= ord(char) <= 90:
        result.append(counter)
    counter += 1

print(result)


