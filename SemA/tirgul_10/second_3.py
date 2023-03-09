import math

class Circle():
    def __init__(self, radius, x,y) :
        if radius<=0:
            raise ValueError("INVALID RADUIS")
        self.center=(x,y)
        self.radius= radius

    def __repr__(self) :
        return f"Circle: The center point is: {self.center} and radius is: {self.radius}"

    def circumference(self):
        return math.pi*2*self.radius

    def area(self):
        return math.pi*(self.radius**2)

    def same_Area(self,ci2):
        c2_area= ci2.area()
        if c2_area== self.area():
            return True
        return False


c1 = Circle(7,1,2)
c2 = Circle(3, 2,4)
print(c1)
c_list=[c1,c2]
print(c1.area())
print(c2.circumference())
print(c1.same_Area(c2))

