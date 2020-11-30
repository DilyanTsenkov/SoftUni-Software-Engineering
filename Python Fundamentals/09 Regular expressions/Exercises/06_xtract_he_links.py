import re

while True:
    string = input()
    if string == "":
        break
    regex = r"(w{3}\.)([a-zA-Z0-9]+[a-zA-Z0-9\-]+?[a-zA-Z0-9]+?\b)(\.[a-z]+)+"

    links = re.finditer(regex, string)

    for link in links:
        print(link.group())
