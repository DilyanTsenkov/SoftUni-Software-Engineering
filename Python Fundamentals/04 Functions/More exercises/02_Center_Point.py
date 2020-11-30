def center_point(x1, y1, x2, y2):
    import math
    first_point = math.sqrt(((x1 - 0) ** 2) + ((y1 - 0) ** 2))
    second_point = math.sqrt(((x2 - 0) ** 2) + ((y2 - 0) ** 2))
    if first_point <= second_point:
        x = x1
        y = y1
    else:
        x = x2
        y = y2
    return f"({int(x)}, {int(y)})"


x1 = input()
y1 = input()
x2 = input()
y2 = input()

print(center_point(float(x1), float(y1), float(x2), float(y2)))
