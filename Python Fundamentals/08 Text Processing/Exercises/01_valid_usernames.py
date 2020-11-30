user_name = input()
user_name = user_name.split(", ")

for name in user_name:
    if 3 <= len(name) <= 16:
        counter = 0
        for char in name:
            if char.isalpha() or char.isdigit() or char == "-" or char == "_":
                counter += 1
                if counter == len(name):
                    print(name)
