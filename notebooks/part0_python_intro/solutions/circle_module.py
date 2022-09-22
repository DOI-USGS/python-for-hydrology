import math


class Circle(object):
    def __init__(self, x, ID):
        self.radius = x
        self.ID = ID

    @property
    def area(self):
        return math.pi * (self.radius ** 2)

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):
        return f"Circle: ID: {self.id}, radius: {self.radius}, " \
               f"area: {self.area}, circumference: {self.circumference}"

    def __truediv__(self, other):
        return self.area / other.area