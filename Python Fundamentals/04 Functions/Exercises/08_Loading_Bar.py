def loading(percent):
    bar = ""
    for i in range(1, 101, 10):
        if i <= number:
            bar += "%"
        else:
            bar += "."
    if number != 100:
        printing = f"{number}% [{bar}]\nStill loading..."
    else:
        printing = f"100% Complete!\n[{bar}]"
    return printing


number = int(input())

print(loading(number))
