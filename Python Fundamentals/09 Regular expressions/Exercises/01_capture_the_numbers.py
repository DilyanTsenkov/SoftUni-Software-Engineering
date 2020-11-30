import re

while True:
    numbers = input()
    if numbers == "":
        break
    regex = r"[0-9]+"
    numbers = re.findall(regex, numbers)
    if numbers:
        print(" ".join(numbers), end=" ")
