import math

class Pos_Point():

    def __init__(self,x=0,y=0):
        # self.my_point=(x,y)
        self.__check_value(x)
        self.__check_value(y)
        self.__x=x
        self.y=y
        self.color="Black"

    def __repr__(self):
        return f"({self.__x},{self.y}) - {self.color} point"

    def change_color(self,new_color):
        self.color=new_color

    def distance(self,other_point):
        x_dis= (self.__x - other_point.__x) ** 2
        y_dis=(self.y-other_point.y)**2
        return math.sqrt(x_dis+y_dis)

    def get_x(self):
        return self.__x

    def set_x(self,new_x):
        self.__check_value(new_x)
        self.__x=new_x

    def __check_value(self,val):
        if val<0:
            raise ValueError("This is a positive point!")

    def __add__(self, other):
        x=self.__x+other.get_x()
        y= self.y+other.y
        return Pos_Point(x,y)

    def __lt__(self, other):
        return self.__x < other.get_x()

p1=Pos_Point(5, 3)
p2=Pos_Point(1, 1)
p3=Pos_Point()
# p4=Pos_Point(-1,-7) - Error!
print(p1)
print(p3)
# print(p4)



p1.change_color("Blue")
p2.change_color("Red")



print(p1)
print(p2)

distance_p3_p2=p2.distance(p3)
print(distance_p3_p2)


# p1.__x=-77
# print(p1.__x)
print(p1.get_x())
# p1.set_x(-77)
p1.set_x(23)
print(p1)

new_p=p1+p2
print(p1)
print(p2)
print(new_p)

if p1<p2:
    print("p1")
else:
    print("p2")
