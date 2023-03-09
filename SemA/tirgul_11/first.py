import math


class Point():
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def distance(self,other_point):
        x_s= (self.x - other_point.__x) ** 2
        y_s = (self.y - other_point.__y) ** 2
        return math.sqrt(x_s + y_s)


class Line():

    def __init__(self,p1,p2):
        self.point1=p1
        self.point2=p2

    def slope(self):
        return (self.point1.__y - self.point2.__y) / (self.point1.__x - self.point2.__x)

    def n(self):
        return self.point1.__y - (self.slope() * self.point1.__x)

    def __repr__(self):
        return f"y={self.slope()}x+{self.n()}"

    def is_on_line(self,other_point):
        x_max= max(self.point1.__x, self.point2.__x)
        y_max= max(self.point1.__y, self.point2.__y)
        y_min= min(self.point1.__y, self.point2.__y)
        x_min= min(self.point1.__x, self.point2.__x)
        if x_min <= other_point.__x <= x_max:
            if y_min <= other_point.__y <= y_max:
                return other_point.__y == self.slope() * other_point.__x + self.n()
        return False




p1=Point(6,9)
p2= Point()
p3=Point(y=4,x=7)
print(p1.distance(p2))
line1=Line(p1,p3)
print(line1)
print(line1.is_on_line(p2))


