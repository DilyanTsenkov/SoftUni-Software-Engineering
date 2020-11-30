first_string = input()
second_string = input()

while True:
    if first_string in second_string:
        second_string = second_string.replace(first_string, "")
    else:
        break

print(second_string)
