class Player():
    def __init__(self,name):
        self.__name=name
        self.__max_live=5
        self.__curr_live=5

    def getName(self):
        return self.__name

    def setName(self,new_name):
        self.__name=new_name

    def getMaxLive(self):
        return self.__max_live

    def getCurrLive(self):
        return self.__curr_live

    def isAlive(self):
        return self.getCurrLive()>0

    def heal(self,amount):
        if type(amount)!=int:
            raise TypeError("only integers!")
        if amount<0:
            raise ValueError("only positive amount")
        if self.__curr_live+amount<=5:
            self.__curr_live+=amount
        else:
            self.__curr_live=5

    def attacked(self):
        self.__curr_live-=1

    def attack(self,other_player):
        if not other_player.isAlive():
            raise ValueError("player is dead")
        other_player.attacked()

    def __repr__(self):
        return f"My name is {self.__name} I have {self.__curr_live} lives"


p1=Player("Ohad")
p2=Player("Eden")
p1.attack(p2)



class FlyingPlayer(Player):
    def __init__(self,name,speed):
        super().__init__(name)
        self.__speed=speed
        self.__max_fly_high=100

    def fly(self):
        print(f"Im {self.getName()}, speed:{self.__speed}, high: {self.__max_fly_high}")

    def setMaxHigh(self,new_high):
        self.__max_fly_high=new_high

    def attacked(self):
        super().attacked()
        self.__speed-=10
        if self.__speed<0:
            self.__speed=1

f1=FlyingPlayer("ohad",4)
f1.fly()
f1.setMaxHigh(55)
f1.fly()


