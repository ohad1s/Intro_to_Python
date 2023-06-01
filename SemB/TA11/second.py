import random


class Player():
    def __init__(self,name):
        self.__name=name
        self.__curr_live=5
        self.__max_live=5

    def __repr__(self):
        return f"My name is: {self.__name} live: {self.__curr_live}"

    def getName(self):
        return self.__name

    def getMaxLive(self):
        return self.__max_live

    def getCurrLive(self):
        return self.__curr_live

    def setName(self,newName):
        self.__name=newName

    def isAlive(self):
        return self.__curr_live>0

    def heal(self,amount):
        if amount<0:
            raise ValueError("amount must be positive!")
        if self.__curr_live + amount <=5:
            self.__curr_live+=amount
        else:
            self.__curr_live=5

    def attacked(self):
        self.__curr_live-=1

    def attack(self,other):
        if not other.isAlive():
            raise ValueError("player is dead!")
        other.attacked()


    def power(self,speed,max_dist):
        return speed*max_dist/self.__curr_live


p1=Player("Maxim")
p2=Player("Shira")
p1.attack(p2)

class FlyingPlayer(Player):
    def __init__(self,name,speed):
        super().__init__(name)
        self.__speed=speed
        self.__max_high=100

    def getSpeed(self):
        return self.__speed

    def getDist(self):
        return self.__max_high

    def fly(self):
        print(f"Im {self.getName()} speed: {self.__speed}, high: {self.__max_high}")

    def set_max_high(self, new_h):
        if new_h<1:
            raise ValueError("cant be negative")
        self.__max_high=new_h

    def attacked(self):
        super().attacked()
        self.__speed-=10
        if self.__speed<=0:
            self.__speed=1

    def minus_speed(self,new_s):
        self.__speed-=new_s

f1=FlyingPlayer("ohad",100)
print(f1)
print(f1.getSpeed())
p1.attack(f1)
print(f1.getSpeed())


class SwimmingPlayer(Player):
    def __init__(self,name,speed):
        super().__init__(name)
        self.__speed=speed
        self.__depth=10

    def getSpeed(self):
        return self.__speed

    def getDist(self):
        return self.__depth

    def swim(self):
        print(f"Im {self.getName()} speed: {self.__speed}, depth: {self.__depth}")

    def set_depth(self,new_d):
        if new_d<1:
            raise ValueError("cant be negative")
        self.__depth=new_d

    def minus_speed(self,new_s):
        self.__speed-=new_s


class Game():
    def __init__(self,p1,s1,p2,s2,p3,s3,p4,s4,joker):
        self.sw1=SwimmingPlayer(p1,s1)
        self.sw2=SwimmingPlayer(p2,s2)
        self.f1=FlyingPlayer(p3,s3)
        self.f2=FlyingPlayer(p4,s4)
        if joker=="s":
            self.joker=SwimmingPlayer("joker",100)
        elif joker=="f":
            self.joker=FlyingPlayer("Joker",100)
        else:
            raise ValueError("must get s or f")
        self.lst=[self.sw1,self.sw2,self.f1,self.f2,self.joker]

    def prize(self):
        x=random.randint(0,len(self.lst)-1)
        self.lst[x].heal(1)

    def punish(self):
        x=random.randint(0,len(self.lst)-1)
        self.lst[x].minus_speed(5)

    def fight(self,name1,name2):
        p1,p2=None,None
        for player in self.lst:
            if name1==player.getName():
                p1=player
            elif name2==player.getName():
                p2=player
        if p1 == None or p2 == None:
            raise ValueError("name not playing")
        if p1.power(p1.getSpeed(), p1.getDist())> p2.power(p2.getSpeed(), p2.getDist()):
            p1.attack(p2)
        else:
            p2.attack(p1)






g1=Game("ohad",5,"ohad",5,"ohad",5,"ohad",5,"s")
print(g1.joker)




