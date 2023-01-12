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
        return Point(self.x+other.x , self.y+other.y)

    def __eq__(self, other):
        return self.x==other.x and self.y==other.y

    def __pow__(self, power):
        return Point(self.x**power,self.y**power)

    def __lt__(self, other):
        return (self.x+self.y)/2 < (other.x+other.y)/2




class Line():

    def __init__(self,p1,x,y):
        self.point1=p1
        self.point2=Point(x,y)

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




# p1=Point(6,9)
# p2= Point()
# p3=Point(y=4,x=7)
# print(p1.distance(p2))
# line1=Line(p1,5,3)
# print(line1)
# print(line1.is_on_line(p2))
#
# def print_x(x):
#     print(x)
#
# print_x("hello")
#
# line1.is_on_line(p1)
# my_str="ohad shirazi is your TA"
# splited_str= my_str.split(" ")
# my_list= [5,6,82,9,1,5,0]
# # new_list= my_list.sort()
# print("mylist", my_list)
# # print("new_list", new_list)
# new_list= sorted(my_list)
# print("new_list", new_list)

p1=Point(5,7)
p2=Point(3,2)
print(p1+p2)
p3= p1+p2
print(p3)
print(p3==p1)
p4=(p3**2)
points_list=[p1,p2,p3,p4]
points_list.sort()
print(points_list)
sorted_points= sorted(points_list,key=lambda p:(p.x,p.y),reverse=True)
string_list= ["dasfs","ehkfgewkfgeklfgwekf","Fafsf","fdsffFSFS","FDSFDSAF","SDFDSKGFKGFEf"]
sorted_strings= sorted(string_list,key=lambda my_string:len(my_string))
print(sorted_strings)
sorted_strings2= sorted(string_list,key=len)
print(sorted_strings2)


