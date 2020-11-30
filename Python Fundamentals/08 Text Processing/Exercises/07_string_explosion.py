text = input()

counter = 0

while True:
    if counter == len(text):
        break
    if text[counter] == ">":
        strength = int(text[counter + 1])
        while strength != 0:
            if text[counter + 1] == ">":
                strength += int(text[counter + 2])
                index = counter + 2
                text = text[0:index:] + text[index::]
                counter += 1
            else:
                index = counter + 1
                text = text[0: index:] + text[index + 1::]
            strength -= 1
            if counter + 1 == len(text):
                break
        counter += 1
    else:
        counter += 1

print(text)