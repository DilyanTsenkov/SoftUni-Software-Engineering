import math

length = float(input())
width = float(input())
rows = math.floor((width - 1) / 0.70)
col = math.floor(length / 1.2)
working_places = rows * col - 3
print(working_places)
