text = input()

counter = 0

while True:
    if counter == len(text) - 1:
        print(text[counter])
        break
    elif text[counter] == text[counter + 1]:
        counter += 1
        continue
    else:
        print(text[counter], end="")
        counter += 1
