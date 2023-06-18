import random


def q2(s):
    s2=s.strip(" ")
    if len(s2)<=1:
        return True
    return s2[0].lower()==s2[-1].lower() and q2(s2[1:-1])

def sol(s):
    if q2(s):
        print("palindrome")
    else:
        print("no")

def q3(lst):
    max_lst=[]
    for i in range(len(lst)):
        curr=[lst[i]]
        for j in range(i+1,len(lst)):
            if lst[j]>curr[-1]:
                curr.append(lst[j])
        if len(curr)>len(max_lst):
            max_lst=curr
    return max_lst

class Block:
    def __init__(self,num1,num2):
        if 0<=num1<=6 and 0<=num2<=6:
            self.__x=num1
            self.__y=num2
        else:
            raise ValueError("must be 0-6")

    def getRight(self):
        return self.__y

    def getLeft(self):
        return self.__x

    def __repr__(self):
        return f"{self.__x} {self.__y}"

    def reverse(self):
        return Block(self.__y,self.__x)

    def check_right(self,other):
        if self.getRight()==other.getRight() or self.getRight()==other.getLeft():
            return True

    def check_left(self,other):
        if self.getLeft()==other.getRight() or self.getLeft()==other.getLeft():
            return True

class Deck:
    def __init__(self):
        self.__d=[]
        for i in range(0,7):
            for j in range(i,7):
                self.__d.append(Block(i,j))

    def getDeck(self):
        return self.__d

    def __repr__(self):
        s=""
        for block in self.__d:
            s+=block
            s+=","
        return s[:-1]

    def draw(self):
        if not self.is_empty():
            x=random.randint(0,len(self.__d)-1)
            # we need -1 because high is included
            b= self.__d.pop(x)
            return b
        print("empty deck")

    def is_empty(self):
        return len(self.__d)==0

class board:
    def __init__(self,block):
        self.__b=[block]

    def __repr__(self):
        s=""
        for block in self.__b:
            s+=block
            s+=","
        return s[:-1]

    def add_right(self,block):
        if self.__b[-1].check_right(block):
            if self.__b[-1].getRight()==block.getLeft():
                self.__b.append(block)
            else:
                self.__b.append(block.reverse())
            return True
        return False

    def add_left(self,block):
        if self.__b[0].check_left(block):
            if self.__b[0].getLeft()==block.getRight():
                self.__b.insert(0,block)
            else:
                self.__b.insert(0,block.reverse())
            return True
        return False
