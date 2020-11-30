import math

flower_m = int(input())
flower_z = int(input())
flower_r = int(input())
cactus = int(input())
present = float(input())
profit = flower_m * 3.25 + flower_z * 4 + flower_r * 3.5 + cactus * 8
profit_with_taxes = profit * 0.95
result = profit_with_taxes - present
if profit_with_taxes >= present:
    print(f'She is left with {math.floor(result)} leva.')
else:
    print(f'She will have to borrow {math.ceil(abs(result))} leva.')
