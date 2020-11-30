string = input()

digit = ""
alpha = ""
symbols = ""

for el in string:
    if el.isdigit():
        digit += el
    elif el.isalpha():
        alpha += el
    else:
        symbols += el

print(f"{digit}\n{alpha}\n{symbols}")
