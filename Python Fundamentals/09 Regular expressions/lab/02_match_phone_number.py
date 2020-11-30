import re

phones = input()
regex = r"(\+[359]+[-][2][-][0-9]{3}[-][0-9]{4}\b)|(\+[359]+ [2] [0-9]{3} [0-9]{4}\b)"
phones = re.finditer(regex, phones)
phones = [p.group(0) for p in phones]

print(*phones, sep=", ")
