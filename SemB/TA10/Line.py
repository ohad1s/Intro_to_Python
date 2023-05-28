from Poss_Point import Pos_Point

class Line():

    def __init__(self,p1,p2):
        if type(p1)!= Pos_Point or type(p2)!= Pos_Point:
            raise TypeError("points muse be positive")

        self.point1=p1
        self.point2=p2

    def __repr__(self): # Y=aX+b
        return f"Y={self.a()}X+{self.b()}"

    def a(self):
        x_dif= self.point1.__x - self.point2.__x
        y_dif = self.point1.y - self.point2.y
        return y_dif/x_dif

    def b(self):
        return self.point1.y-(self.a() * self.point1.__x)

    def is_on_line(self,point):
        x_min=min(self.point1.__x, self.point2.__x)
        y_min=min(self.point1.y,self.point2.y)
        x_max=max(self.point1.__x, self.point2.__x)
        y_max=max(self.point1.y,self.point2.y)
        if x_min <= point.__x <= x_max:
            if y_min <= point.y <= y_max:
                return point.y == self.a() * point.__x + self.b()
        return False


p1 = Pos_Point(1, 2)
p2 = Pos_Point(7, 5)
p3 = Pos_Point(11, 15)
line1=Line(p1,p2)
print(line1)
print(line1.is_on_line(p3))


