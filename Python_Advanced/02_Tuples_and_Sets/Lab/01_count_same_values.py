values = list(float(el) for el in input().split())

values_counter = {}

for value in values:
    if value not in values_counter:
        values_counter[value] = 0
    values_counter[value] += 1

for key, value in values_counter.items():
    print(f"{key} - {value} times")
