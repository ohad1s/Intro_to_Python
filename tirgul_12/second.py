import math


class Point():
    def __init__(self, x=0,y=0):
        self.x=x
        self.y=y

    def __repr__(self):
        return f"({self.x},{self.y})"

    def distance(self,other_point):
        x_s= (self.x - other_point.x)**2
        y_s = (self.y - other_point.y)**2
        return math.sqrt(x_s + y_s)

    def __add__(self, other):
        return Point(self.x+other.x,self.y+other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __radd__(self, other):
        if type(other)!=int:
            raise TypeError("read only int!")
        return Point(self.x+other, self.y+other)

    def __lt__(self, other):
        return self.x < other.x


class Line():

    def __init__(self,p1,x,y):
        self.point1=p1
        self.point2=Point(x,y)
        self.color="Black"

    def slope(self):
        return (self.point1.y-self.point2.y)/(self.point1.x-self.point2.x)

    def n(self):
        return self.point1.y-(self.slope()*self.point1.x)

    def __repr__(self):
        return f"y={self.slope()}x+{self.n()}"

    def is_on_line(self,other_point):
        x_max= max(self.point1.x, self.point2.x)
        y_max= max(self.point1.y, self.point2.y)
        y_min= min(self.point1.y, self.point2.y)
        x_min= min(self.point1.x, self.point2.x)
        if x_min <= other_point.x <= x_max:
            if y_min <= other_point.y <= y_max:
                return other_point.y == self.slope()*other_point.x + self.n()
        return False

p1=Point(6,9)
p2= Point(3,2)
p3=Point(y=4,x=7)
print(p1.distance(p2))
line1=Line(p1,5,3)
print(line1)
print(line1.is_on_line(p2))
my_str= "ohad yossi dani"
my_str.split(" ")
mylist=[1,4,8,2,4,9,0]
x= mylist.sort()
print(x)
print(mylist)
new_list= sorted(mylist)
p4 = p1+p2
print(p4)
x=5
y=3
print(x==y)
print(p3==p4)
p5=2+p1
# p6=p1+2
print(p5)
# print(p6)
# p6= "yossi"+p1
p7=p5+p3
print(p7)
points_list=[p1,p2,p3,p4,p5,p7]
# points_list.sort()
# print(points_list)
sorted_points= sorted(points_list,reverse=True,key=lambda p:(p.y,p.x))
print(sorted_points)
strings_list=["fdsfdsfsf","adfs","fsdfdsfs","FGADFSGAGRsgW","SDGDSNKFHDSF","sdfnjs"]
# x= strings_list.sort()
sorted_string= sorted(strings_list,key=len)
print(sorted_string)
str__= sorted("593486139")
print(str__)
