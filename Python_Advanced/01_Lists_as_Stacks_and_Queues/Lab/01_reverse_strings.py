text = input()

s = []

for n in range(len(text) - 1, -1, -1):
    s.append(text[n])

print("".join(s))
