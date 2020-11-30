def line(x1, y1, x2, y2, x3, y3, x4, y4):
    import math
    first_line = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))
    second_line = math.sqrt(((x4 - x3) ** 2) + ((y4 - y3) ** 2))
    if first_line >= second_line:
        first_point = math.sqrt(((x1 - 0) ** 2) + ((y1 - 0) ** 2))
        second_point = math.sqrt(((x2 - 0) ** 2) + ((y2 - 0) ** 2))
        if first_point <= second_point:
            first_point_x = x1
            first_point_y = y1
            second_point_x = x2
            second_point_y = y2
        else:
            first_point_x = x2
            first_point_y = y2
            second_point_x = x1
            second_point_y = y1
    else:
        first_point = math.sqrt(((x3 - 0) ** 2) + ((y3 - 0) ** 2))
        second_point = math.sqrt(((x4 - 0) ** 2) + ((y4 - 0) ** 2))
        if first_point <= second_point:
            first_point_x = x3
            first_point_y = y3
            second_point_x = x4
            second_point_y = y4
        else:
            first_point_x = x4
            first_point_y = y4
            second_point_x = x3
            second_point_y = y3
    return f"({int(first_point_x)}, {int(first_point_y)})({int(second_point_x)}, {int(second_point_y)})"


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(line(x1, y1, x2, y2, x3, y3, x4, y4))
