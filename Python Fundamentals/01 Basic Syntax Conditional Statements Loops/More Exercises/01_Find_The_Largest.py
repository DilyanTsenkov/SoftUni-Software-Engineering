number = input()

tank = []

for i in number:
    tank.append(int(i))
tank.sort(reverse=True)

for n in range(len(tank)):
    print(tank[n], end="")
