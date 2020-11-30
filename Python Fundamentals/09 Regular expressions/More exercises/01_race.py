import re
from collections import Counter

participants = input().split(", ")

score = {}
while True:
    info = input()
    if info == "end of race":
        break

    regex = r"[A-Za-z0-9+]"
    name_distance = re.findall(regex, info)

    name = ""
    distance = 0
    for char in name_distance:
        if char.isalpha():
            name += char
        else:
            distance += int(char)
    if name in participants:
        if name not in score:
            score[name] = distance
        else:
            score[name] += distance

score = Counter(score).most_common(3)
places = ["1st", "2nd", "3rd"]

for n in range(len(places)):
    print(f"{places[n]} place: {score[n][0]}")