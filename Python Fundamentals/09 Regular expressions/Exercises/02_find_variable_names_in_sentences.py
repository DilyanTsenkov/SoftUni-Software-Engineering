import re

names = input()
result = ""

regex = r"(^|(?<= ))_(?P<name>[a-zA-Z0-9]+)($|(?= ))"

names = re.finditer(regex, names)
for name in names:
    n = name.groupdict()
    result += f"{n['name']},"

print(result[:-1])
