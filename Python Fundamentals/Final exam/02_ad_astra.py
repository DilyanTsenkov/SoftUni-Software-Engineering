import re

string = input()

regex = r"(?P<symbol>[|/|#])(?P<name>([A-Za-z\s]+))(?P=symbol)(?P<date>([0-9]{2}/[0-9]{2}/[0-9]{2}))(?P=symbol)(?P<cal>([0-9]{1,5}))(?P=symbol)"

calories = 0
counter = 1
items = {}

finder = re.finditer(regex, string)
for item in finder:
    d = item.groupdict()
    items[counter] = {"name": d["name"], "date": d["date"], "cal": d["cal"]}
    counter += 1
    calories += int(d["cal"])

days = calories // 2000

print(f"You have food to last you for: {days} days!")
for v in items.values():
    print(f'Item: {v["name"]}, Best before: {v["date"]}, Nutrition: {v["cal"]}')
