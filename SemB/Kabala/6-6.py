import math


class Circle:
    def __init__(self,x,y,radius:float):
        if radius <=0:
            raise ValueError("radius must be positive")
        self.__r=radius
        self.center=(x,y)

    def __repr__(self):
        return f"radius: {self.__r}, center point: {self.center}"

    def get_radius(self):
        return self.__r

    def set_radius(self,newR):
        if newR<=0:
            raise ValueError("radius must be positive")
        self.__r=newR

    def perimeter(self):
        return 2*math.pi*self.__r

    def area(self):
        return math.pi*(self.__r**2)

    def are_the_same(self,other):
        return self.__r==other.get_radius() and self.center==other.center

# c1=Circle(5,3,3.3)
# c2=Circle(8,4,7)
# print(c1)
# if c1.area()>c2.area():
#     print(c1, c1.area())
# else:
#     print(c2,c2.area())
# print(c1.are_the_same(c2))
# c2.are_the_same(c1)

def movies_dict(lst):
    res={}
    for dicti in lst:
        dir=dicti["director"] # yossi
        movie=dicti["name"]   # shrek
        res[dir]=res.get(dir,[])
        res[dir].append(movie)
    return res


# lst=[{"director":"yossi","name":"shrek","rank":5},{"director":"yossi","name":"shrek2","rank":7}
#      ,{"director":"dani","name":"madagascar","rank":8}]
# res=movies_dict(lst)
# print(res)


# HourGlass:
def HourGlass(n):
    space=0
    for i in range(n,0,-2):
        # print(space*" "+i*"*")
        for sp in range(space):
            print(" ", end="")
        for star in range(i):
            print("*",end="")
        print()
        space+=1
    if n%2==0:
        s=2
    else:
        s=3
        space-=1
    for i in range(s,n+1,2):
        space-=1
        for sp in range(space):
            print(" ", end="")
        for star in range(i):
            print("*",end="")
        print()

HourGlass(9)

