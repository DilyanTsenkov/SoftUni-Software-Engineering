import math

X = int(input())
Y = float(input())
Z = int(input())
workers = int(input())
for_wine = X * 0.4
grapes_for_wine = for_wine * Y
liters_wine = grapes_for_wine / 2.5
result = liters_wine - Z
if Z > liters_wine:
    print(f'It will be a tough winter! More {math.floor(abs(result))} liters wine needed.')
else:
    print(f'Good harvest this year! Total wine: {math.floor(liters_wine)} liters.')
    print(f'{math.ceil(result)} liters left -> {math.ceil(result / workers)} liters per person.')
