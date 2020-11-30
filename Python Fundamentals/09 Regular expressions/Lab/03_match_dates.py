import re

dates = input()

regex = r"\b(?P<day>[0-9]{2})(?P<separator>[-\./])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>[0-9]{4})"

dates = re.finditer(regex, dates)

for date in dates:
    d = date.groupdict()
    print(f"Day: {d['day']}, Month: {d['month']}, Year: {d['year']}")
