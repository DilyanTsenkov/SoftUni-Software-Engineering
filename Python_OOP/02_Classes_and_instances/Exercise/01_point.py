from math import sqrt


class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        d = (self.x - x) ** 2 + (self.y - y) ** 2
        return sqrt(d)


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))
