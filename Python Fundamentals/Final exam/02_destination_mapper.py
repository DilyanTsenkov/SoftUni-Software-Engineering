import re

string = input()

regex = r"(?P<symbol>=|/)(?P<place>([A-Z][A-Za-z]{2,}))(?P=symbol)"

places = []
travel_points = 0

data = re.finditer(regex, string)
for item in data:
    d = item.groupdict()
    travel_points += len(d["place"])
    places.append(d["place"])

places = ", ".join(places)

print(f"Destinations: {places}")
print(f"Travel Points: {travel_points}")
