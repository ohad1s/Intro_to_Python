import math

from Summer.TA7.Point import Positive_Point


class Circle:
    def __init__(self,x=0,y=0,r=1):
        if r<=0:
            raise ValueError("...")
        self.__radius=r
        self.__center=Positive_Point(x,y)

    def get_radius(self):
        return self.__radius

    def get_center(self):
        return self.__center

    def set_radius(self,new_radius):
        if new_radius>0:
            self.__radius=new_radius

    def set_center(self,new_center):
        self.__center=new_center

    def set_center_by_xy(self, x,y):
        self.__center = Positive_Point(x,y)

    def __repr__(self):
        return f"Circle:\ncenter point: {self.__center}\nradius: {self.__radius}"

    def area(self):
        return math.pi*(self.__radius**2)

    def are_same_area(self,other_circle):
        return self.area()==other_circle.area()

    def are_the_same_radius(self,other):
        return self.__radius==other.get_radius()

    def check_values(self,other_circle):
        print(self.__radius)
        print(other_circle.get_radius())


c1=Circle(2,3,10)
c2=Circle(5,1)
c3=Circle(4)
c4=Circle()
# print(c1.__radius)
# print(c1.__center)
# c1.radius=10
# c1.radius=-5
print(c1.get_radius())
c1.set_radius(-5)
print(c1.get_radius())
c1.set_radius(200)
print(c1.get_radius())
print(c1)
print(type(c1))
c1.are_the_same_radius(c2)
c2.set_radius(7)
c7=Circle(3,3,3)






# def bdika(a,b):
#     return a+b
# bdika(3,2)

# "ab-cd-ed".split("-")