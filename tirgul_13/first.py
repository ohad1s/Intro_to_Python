import math


class Point():
    def __init__(self, x=0, y=0):
        self.__valid_input(x)
        self.__x = x  # private
        self.__valid_input(y)
        self.__y = y

    def __repr__(self):
        return f"({self.__x},{self.__y})"


    def getY(self):
        return self.__y

    def setY(self, newY):
        self.__valid_input(newY)
        self.__y=newY


    def getX(self):
        return self.__x

    def setX(self, new_x):
        self.__valid_input(new_x)
        self.__x = new_x


    def __valid_input(self, value):
        if value<0:
            raise ValueError("only positive values!")

    def distance(self, other_point):
        x_s = (self.__x - other_point.__x) ** 2
        y_s = (self.__y - other_point.__y) ** 2
        return math.sqrt(x_s + y_s)

    def __add__(self, other):
        return Point(self.__x + other.__x, self.__y + other.__y)

    def __eq__(self, other):
        return self.__x == other.__x and self.__y == other.__y

    def __pow__(self, power):
        return Point(self.__x ** power, self.__y ** power)

    def __lt__(self, other):
        return (self.__x + self.__y) / 2 < (other.__x + other.__y) / 2


p1 = Point(1, 2)
# p2= Point(-2,3)
# print(p1.__x)
print(p1.getX())
# p1.__x=10
p1.setX(3)
print(p1)
# p1.setX(-5) -> Error


