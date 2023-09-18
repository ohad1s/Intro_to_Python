class Robot:
    next_id=1
    def __init__(self,name):
        self.__id=Robot.next_id
        Robot.next_id+=1
        self.__name=name
        self.__battery=100

    def getBattery(self):
        return self.__battery

    def charge(self,min):
        if min<1:
            raise ValueError("minutes must be positive!")
        if self.__battery<100:
            self.__battery+=min
            if self.__battery>100:
                self.__battery=100

    def sing(self):
        print(" I’m gonna stand here like a unicorn")
        self.__battery-=5

    def __repr__(self):
        rep= f"My name is {self.__name}, id: {self.__id}"
        if self.__battery==100:
            rep+=", and I'm fully charged!"
        if self.__battery<20:
            rep+=", please charge me!!!"
        return rep

    def lose_battery(self,num):
        self.__battery-=num
        if self.__battery<0:
            self.__battery=0

    def fight(self,other):
        if self.__battery>other.getBattery():
            self.__battery-=5
            other.lose_battery(10)
        else:
            self.__battery-=10
            other.lose_battery(5)

class SiameseRobot(Robot):

    def __init__(self,name):
        super().__init__(name)
        self.second_robot=Robot(name)

    def __repr__(self):
        return f"I'm a Siamese Robot: {super().__repr__()}" \
               f" and my second Robot is: {self.second_robot}"


# r1=Robot("ra")



