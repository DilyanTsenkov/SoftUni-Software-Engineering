import re

numbers = input()
regex = r"(^|(?<= ))-?[0-9]+(\.[0-9]+)?($|(?= ))"

numbers = re.finditer(regex, numbers)
numbers = [n.group() for n in numbers]

print(" ".join(numbers))
