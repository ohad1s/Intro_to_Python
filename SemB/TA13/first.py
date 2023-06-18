import random


def q2(s):
    s2=s.strip(" ")
    if len(s2)<=1:
        return True
    return s2[0].upper()==s2[-1].upper() and q2(s2[1:-1])

print(q2("A man a plan D Canal Panama"))

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

lst= [ 18,101, 7, 3, 5, 2, 9, 10]
lst.reverse()
print(q3(lst ))


class Block:
    def __init__(self,x,y):
        if 0<=x<=6 and 0<=y<=6:
            self.x=x
            self.y=y
        else:
            raise ValueError("must be between 0 to 6")

    def __repr__(self):
        return f"{self.x} {self.y}"

    def reverse(self):
        return Block(self.y,self.x)

    def check_right(self,other):
        if self.y==other.x:
            return True
        return False

    def check_left(self,other):
        if self.x==other.y:
            return True
        return False

class Deck:
    def __init__(self):
        self.d=[]
        for i in range(0,7):
            for j in range(0,7):
                self.d.append(Block(i,j))

    def __repr__(self):
        s=""
        for block in self.d:
            s+=block
            s+=","
        return s[:-1]

    def draw(self):
        if not self.is_empty():
            x= random.randint(0,len(self.d)-1)
            block= self.d.pop(x)
            return block
        print("empty deck")

    def is_empty(self):
        return len(self.d)==0


class Board():
    def __init__(self,block):
        self.board=[block]

    def __repr__(self):
        s=""
        for block in self.board:
            s+=block
            s+=","
        return s[:-1]

    def add_left(self,b):
        curr=self.board[0]
        if curr.check_left(b):
            self.board.insert(0,b)
            return True
        return False

    def add_right(self,b):
        curr=self.board[-1]
        if curr.check_right(b):
            self.board.append(b)
            return True
        return False




