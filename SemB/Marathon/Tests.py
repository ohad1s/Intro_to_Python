import math


def insert(L,e):
    for i in range(len(L)-1):
        if L[i]<=e<=L[i+1]:
            L.insert(i+1,e)
            break
    else:
        L.append(e)

def max_num(L):
    if len(L)==1:
        return L[0]
    maxi_rec=max_num(L[1:])
    if maxi_rec>L[0]:
        return maxi_rec
    return L[0]


def select_gift(dict1,dict2):
    dict3=dict1.copy()
    for k , v in dict2.items():
        dict3[k]=dict3.get(k,0)+v
    maxi=max(dict3.values())
    lst=[]
    for k, v in dict3.items():
        if v==maxi:
            lst.append(k)
    lst.sort()
    return lst

class Account:

    def __init__(self,amt):
        if type(amt) in [int,float]:
            self.__balance=amt
        else:
            raise TypeError

    def deposite(self,amt):
        self.__balance+=amt

    def withdraw(self,amt):
        if amt>self.__balance:
            return False
        self.__balance-=amt
        return True

    def get_balance(self):
        return self.__balance


class SavingAccount(Account):

    def __init__(self,balance,interest_rate):
        super.__init__(balance)
        if type(interest_rate) in [int, float]:
            self.rate=interest_rate
        else:
            raise TypeError

class CheckingAccount(Account):

    def __init__(self,amt,protect):
        super.__init__(amt)
        if type(protect)==SavingAccount:
            self.protect=protect
        else:
            raise TypeError


    def withdraw(self,amt):
        if self.get_balance()<amt:
            if self.get_balance()+self.protect.get_balance()<amt:
                return False
            self.protect.__balance-=(amt-self.get_balance())
            self.__balance=0
            return True
        self.__balance-=amt
        return True


class customer:

    def __init__(self,first,last):
        self.__first=first
        self.__last=last
        self.__saving=None
        self.__checking=None

    def set_saving_account(self,amt, interest_rate):
        self.__saving=SavingAccount(amt,interest_rate)

    def set_checking_account(self,amt):
        self.__checking=CheckingAccount(amt,self.__saving)

    def __repr__(self):
        return f"{self.__first} {self.__last}:\n" \
               f"checking account balance: {self.__checking.get_balance()}\n" \
               f"saving account balance: {self.__saving.get_balance()}"




def maxNum(s1:str) -> int:
    maxi=0
    temp=0
    for c in s1:
        if c.isdigit():
            temp*=10
            temp+=int(c)
        else:
            if temp>maxi:
                maxi=temp
            temp=0
    # return maxi
    return max(maxi,temp)



def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

def sin(x,accuracy):
    sin=0
    n=1
    pair = ((x**n)/factorial(n))-((x**(n+2))/factorial(n+2))
    while accuracy < pair:
        sin+=pair
        n+=4
        pair = ((x ** n) / factorial(n)) - ((x ** (n + 2)) / factorial(n + 2))
    return sin


def numOfAdd(x,epsilon):
    sin=0
    n=1
    counter=0
    pair = ((x ** n) / factorial(n)) - ((x ** (n + 2)) / factorial(n + 2))
    while abs(sin-math.sin(x)) > epsilon:
        sin+=pair
        counter+=2
        n+=4
        pair = ((x ** n) / factorial(n)) - ((x ** (n + 2)) / factorial(n + 2))
    return counter


def median(lst):
    lst.sort()
    if len(lst)%2==0:
        return (lst[len(lst)//2]+lst[(len(lst)//2)-1])/2
    return lst[len(lst)//2]


def product(x,y):
    if y==0:
        return 0
    if y==1:
        return x
    return x+product(x,y-1)

def printCapital(s1:str):
    sen=s1.split(" ")
    my_str=""
    for word in sen:
        if word[0].isupper() and word[-1].isupper():
            my_str+=word
            my_str+=" "
    # return my_str[0:-1]
    my_str.strip(" ")
    return my_str

def pascal(x):
    if x==0:
        return
    if x==1:
        print(1)
        return
    if x==2:
        print("1")
        print("1,1")
        return

    pas=[[1],[1,1]]
    for i in range(x-2):
        lst=[1]
        for index in range(len(pas[-1])-1):
            lst.append(pas[-1][index]+pas[-1][index+1])
        lst.append(1)
        pas.append(lst)

    for line in pas:
        for number in line:
            print(number, end=" ")
        print()

    print(pas)


def pascal2(x):
    if x==0:
        return
    if x==1:
        print(1)
        return
    if x==2:
        print("1")
        print("1,1")
        return
    pas = [1,1]
    new_line=[]
    for i in range(x - 2):
        print(1,end=" ")
        new_line.append(1)
        for index in range(len(pas)-1):
            to_app=pas[i]+pas[i+1]
            new_line.append(to_app)
            print(to_app,end=" ")
        new_line.append(1)
        print(1)
        pas=new_line
        new_line = []




def mat(c, r, c1, c2):
    my_mat=[]
    for i in range(r):
        my_mat.append([])
        for j in range(c):
            my_mat[i].append("")

    start = 0
    row = r - 1
    col = c - 1
    sign = c1

    while start <= row and start <= col:
        for i in range(start, row + 1):
            my_mat[i][start] = sign
            my_mat[i][col] = sign

        for j in range(start, col + 1):
            my_mat[start][j] = sign
            my_mat[row][j] = sign

        row -= 1
        col -= 1
        start += 1

        if sign == c1:
            sign = c2
        else:
            sign = c1

    str_mat = ""
    flag = True
    for i in range(r):
        if i == r - 1:
            flag = False
        for j in range(c):
            str_mat += my_mat[i][j]
        if flag:
            str_mat += "\n"

    print(str_mat)

# mat(8,6,"*","@")
pascal(10)

def RPS(txt1,txt2):
    f1= open(txt1,"r")
    s1=f1.read()
    player1= s1.split(",")
    f1.close()
    f2= open(txt2,"r")
    player2=f2.readlines()
    f2.close()
    counter1=0
    counter2=0
    tie=0
    stri="RPS"
    dict1={}
    for i in range(100):
        a=player1[i]
        b=player2[i]


class Item:

    def __init__(self,name,id,volume):
        self.__id=id
        self.__name=name
        self.__volume=volume

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_volume(self):
        return self.__volume

    def set_volume(self,x,y,z):
        self.__volume=x*y*z

    def __repr__(self):
        return f"{self.__name},{self.__id},{self.__volume}"


class Truck:

    def __init__(self,name,id,cap):
        self.__name=name
        self.__id=id
        self.__capacity=cap
        self.itemList=[]
        self.__curr=0

    def load(self,item:Item)->bool:
        if self.__capacity-self.__curr<item.get_volume():
            return False
        self.__curr+=item.get_volume()
        self.itemList.append(item)
        return True

    def dispatch(self,item):
        if item in self.itemList:
            self.itemList.remove(item)
            return True
        return False

    def get_capacity(self):
        return self.__curr

    def __repr__(self):
        return f"{self.__id}"

class PickupTruck(Truck):

    def __init__(self,name,id,cap):
        super.__init__(name,id,cap/2)


def orderTrucks(itemsList,avgCap):
    total=0
    for item in itemsList:
        total+=item.get_volume()
    num=total/avgCap
    if num%1==0:
        return num
    return (num//1)+1

def load_trucks(trucks ,items):
    i=0
    it = items.pop()
    while len(items)>0:
        t=trucks[i]
        while (t.load(it)):
            if len(items)==0:
                break
            it=items.pop()
        i+=1


def suffix(lst,k):
    dict1={}
    for i, s in enumerate(lst):
        ks=s[-k:]
        dict1[ks]=dict1.get(ks,[]).append(i)

    return dict1

def suffix_prefix(lst,k):
    dict1=suffix(lst,k)
    for i , s in enumerate(lst):
        pref=s[:k]
        curr_lst=dict1.get(pref,[])
        if len(curr_lst)>0:
            if len(curr_lst)==1:
                if curr_lst[0]!=i:
                    return True
            return True