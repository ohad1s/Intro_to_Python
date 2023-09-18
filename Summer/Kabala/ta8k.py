class Point:

    point_counter=0

    def __init__(self,x,y):
        self.__x=x
        self.__y=y
        self.__color="Black"
        Point.point_counter+=1

    def change_color(self,new_color):
        self.__color=new_color

    def __repr__(self):
        return f"{self.__color} point: ({self.__x},{self.__y})"

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self,new_x):
        self.__x=new_x

    def split(self):
        return (self.__x,self.__y)

    def __add__(self, other):
        if isinstance(other,Point):
            return Point(self.__x+other.get_x(),self.__y+other.get_y())
        if isinstance(other,int):
            return Point(self.__x+other,self.__y+other)
        else:
            raise ValueError

    def copy(self):
        return Point(self.__x,self.__y)

print(f"counter0: {Point.point_counter} ")
p1=Point(5,3)
print(p1)
# p1.x=5
print(f"counter1: {Point.point_counter} ")
p2=Point(7,1)
print(f"counter2: {Point.point_counter} ")

print(p2)
str_p2=str(p2)

# print(p2.__x)
print(p2.get_x())

# print(p2.__y)
print(p2.get_y())


# p2.__color="Blue"
p2.change_color("Blue")

# p2.__x=10
print(p2)
p2.set_x(10)
print(p2)

val=10+3
p3=p1+p2

my_lst="ohad,ohad,dannit".split(",")
my_tup=p2.split()

p4=p1+10

# by reference:
print(p1)
p8=p1
p8.set_x(17)
print(p8)
print(p1)

# by value:
p9=p1.copy()




# lists by reference:
lst1=[1,2,3]
lst2=lst1
lst2.append(4)
print(lst2)
print(lst1)

# list by value:
l1=[1,2,3]
l2=l1.copy()
l2.append(4)
print(l1)
print(l2)

print(f"counter: {p9.point_counter} ")
print(f"counter: {p1.point_counter} ")