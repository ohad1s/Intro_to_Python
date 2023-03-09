import math
import random


class Point():
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y
        self.z=random.randint(1,100)

    def __repr__(self):
        return f"({self.x},{self.y})"

    def distance(self, other_point):
        x_s= (self.x - other_point.__x) ** 2
        y_s= (self.y - other_point.__y) ** 2
        return math.sqrt(x_s+y_s)

class Line():
    def __init__(self, point1_val, point2):
        if type(point1_val)!=Point:
            raise TypeError("NOT A POINT")
        if type(point2)!=Point:
            raise TypeError("NOT A POINT")
        self.point1=point1_val
        self.point2=point2

    def a(self):
        return (self.point1.__y - self.point2.__y) / (self.point1.__x - self.point2.__x)
    def b(self):
        return self.point1.__y - (self.a() * self.point1.__x)

    def __repr__(self):
        return f"y={self.a()}x+{self.b()}"

    def is_on_line(self,point):
        x_min= min(self.point1.__x, self.point2.__x)
        y_min= min(self.point1.__y, self.point2.__y)
        y_max= max(self.point1.__y, self.point2.__y)
        x_max= max(self.point1.__x, self.point2.__x)
        if x_min <= point.__x <= x_max:
            if y_min <= point.__y <= y_max:
                return point.__y == (self.a() * point.__x) + self.b()
        return False



p1=Point(7,9)
p2=Point(3,4)
p3= Point()
p4 =Point(y=7,x=8)
print(p1)
print(p1.distance(p2))
line1= Line(p1,p2)
print(line1)
line2=Line(Point(1,2), Point(3,4))
print(line1.is_on_line(p3))
# line3= Line(p1, (5,2))

# x1=input("enter a value")
# x2=input("enter a value")
# y1=input("enter a value")
# y2=input("enter a value")
# p11= Point(x1,y1)






