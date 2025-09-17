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



class Pizza(Circle):
    def __init__(self, x, ID, cost):
        super().__init__(x, ID)
        self.cost = cost

    @property
    def price_per_sq_inch(self):
        return self.cost / self.area

    def __floordiv__(self, other):
        """
        Using floor division to add another option for diving pizza price per sq inch.

        This is because there really isn't another good option
        """
        return self.price_per_sq_inch / other.price_per_sq_inch

