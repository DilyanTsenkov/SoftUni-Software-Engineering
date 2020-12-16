import re

number = int(input())

for n in range(number):
    message = input()
    regex = r"(?P<symbol>@|\*)(?P<tag>[A-Z][a-z]{2,})(?P=symbol): \[(?P<one>[A-Za-z])\]\|\[(?P<two>[A-Za-z])\]\|\[(?P<three>[A-Za-z])\]\|$"
    finder = re.findall(regex, message)
    items = re.finditer(regex, message)
    if not finder:
        print("Valid message not found!")
    else:
        for item in items:
            d = item.groupdict()
            print(f"{d['tag']}: {ord(d['one'])} {ord(d['two'])} {ord(d['three'])}")
