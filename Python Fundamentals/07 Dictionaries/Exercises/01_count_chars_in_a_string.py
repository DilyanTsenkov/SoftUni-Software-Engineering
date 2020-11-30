string = input()

counter = {}

for char in string:
    if char == " ":
        continue

    counter_key = char

    if counter_key not in counter:
        counter[counter_key] = 1
    else:
        counter[counter_key] += 1

for counter_key, value in counter.items():
    print(f"{counter_key} -> {value}")
