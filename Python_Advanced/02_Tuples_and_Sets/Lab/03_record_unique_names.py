n = int(input())

names = []

for _ in range(n):
    name = input()
    names.append(name)

names = set(names)

for el in names:
    print(el)
