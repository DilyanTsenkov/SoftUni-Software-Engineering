words = input().lower().split()

odd = {}

for word in words:
    if word not in odd:
        odd[word] = 1
    else:
        odd[word] += 1

for key, values in odd.items():
    if int(values) % 2 != 0:
        print(key, end=" ")
