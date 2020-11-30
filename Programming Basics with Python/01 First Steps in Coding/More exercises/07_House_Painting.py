x = float(input())
y = float(input())
h = float(input())

front_wall = x * x - 1.2 * 2
rear_wall = x * x
left_wall = x * y - 1.5 * 1.5
right_wall = x * y - 1.5 * 1.5
green_paint = (front_wall + rear_wall + left_wall + right_wall) / 3.4
front_roof = x * h/2
side_roof = x * y
red_paint = (front_roof * 2 + side_roof * 2) / 4.3
print(f'{green_paint:.2f}')
print(f'{red_paint:.2f}')
