class Gun:
    __s_number=[1]
    def __init__(self):
        self.__serial_num=len(Gun.__s_number)
        Gun.__s_number.append(self.__serial_num+1)

    def fire(self):
        return "gun fired"

    def get_serial(self):
        return self.__serial_num

class LaserGun(Gun):

    def __init__(self,color):
        if type(color)!=str:
            raise TypeError("color must be a str")
        super().__init__()
        self.__color=color

    def fire(self):
        return f"{self.__color} laser gun fired!"


gun=Gun()
print(gun.fire())
l=LaserGun("black")
print(type(l)==Gun)
print(isinstance(l,Gun))
print([1,2,3]+[4,5,6])


