class Positive_Point:

    def __init__(self,my_x=0,y=0):
        if my_x<0 or y<0:
            raise ValueError("must be a positive value")
        self.__x=my_x
        self.__y=y
        self.__name="p"

    def __repr__(self):
        return f"({self.__x},{self.__y})"

    def getX(self):
        return self.__x

    def getY(self):
        return self.__y

    def setX(self,new_x):
        if new_x<0:
            raise ValueError("....")
        self.__x=new_x

    def setY(self,new_y):
        if new_y<0:
            raise ValueError("....")
        self.__y=new_y

    def distance(self,other_point):
        if type(other_point)!=Positive_Point:
            raise TypeError("...")
        return ((self.__x-other_point.getX())**2 + (self.__y-other_point.getY())**2)**0.5

    def __add__(self, other):
        new_x=self.__x+other.getX()
        new_y= self.__y+other.getY()
        return Positive_Point(new_x,new_y)


# class line:
#
#     def __init__(self,p1,p2):
#         self.p1=p1
#         self.p2=p2
        # etc....


p1=Positive_Point()
p2=Positive_Point(1)
p3=Positive_Point(3,2)
p4=Positive_Point(y=4,my_x=5)
# p5=Positive_Point(-1,2) Error
print(p1)
p2_str=str(p2)
print(p2_str)
print(type(p2_str))
# print("(7,3)")
# print(p2.__y)
# print(p3.__x)
# p2.x=1
# p4.y=-3
print(p1.getX())
print(p3.getY())
p3.setY(17)
print(p3)
dist=p1.distance(p3)
print(dist)
print(5+7)
print("=========")
print(p1)
print(p2)
print(p1+p2)


#
# def add(a,b):
#     return a+b
#
# add(3,4)
#
# lst=[1,2,3]
# lst.append(4)
# lst1="ab-cd-ef".split("-")



