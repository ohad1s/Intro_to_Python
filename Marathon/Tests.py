# ----------- 11/7/21 --------------------
import random
import string


def insert(L:list,e):
    L.append(e)
    L.sort()

 # [1,2,2,3,4,5,5,6,7] 4

def insert_2(L:list,e):
    for i in range(len(L)):
        if e<L[i]:
            L.insert(i,e)
            return
    L.append(e)

L=[1,2,2,3,4,5,5,6,7]
insert_2(L,8)
# print(L)

def max_num(L:list):
    if len(L)==1:
        return L[0]
    maxi=L[0]
    maxi_2=max_num(L[1:])
    if maxi>maxi_2:
        return maxi
    else:
        return maxi_2

def max_num_helper(L,maxi):
    if L[0]>maxi:
        maxi=L[0]
        return max_num_helper(L[1:],maxi)

def max_num_2(L: list):
    return max_num_helper(L,L[0])

def select_gift(good_rating,want_rating):
    sums={}
    for k , v in good_rating.items():
        sums[k]=v
    for k, v in want_rating:
        if k in sums.keys():
            sums[k]+=v  # sums[k] = sums[k]+v
        else:
            sums[k]=v
    p_list=[]
    max_rating=0
    for product, rating in sums:
        if rating>max_rating:
            p_list=[]
            p_list.append(product)
            max_rating=rating
        elif rating==max_rating:
            p_list.append(product)

    p_list.sort()
    return p_list

# primitive vars: int float, str, bool
# a=[1,2,3]
# b=a
# b.append(4)
# a -> [1,2,3,4]


# 4 :
# a - [[5,4],[5,4]]
# b- error
# c- error


# ------------ 2/3/21 ----------------
def printCapital(s1:str):
    my_words= s1.split(" ")
    new_str=""
    for word in my_words:
        if word[0].isupper() and word[-1].isupper():
            new_str+=word
            new_str+=" "
    return new_str

def sumNum(n):
    if n<10:
        return n
    return (n%10)+sumNum(n//10)


class File():
    def __init__(self,name):
        self.name=name
        self.isOpen=False

    def __repr__(self):
        return f"file name: {self.name}, isOpen?: {self.isOpen}"

    def isOpen(self):
        return self.isOpen

    def open(self):
        self.isOpen=True

    def close(self):
        self.isOpen=False

class RestrictedFile(File):

    def __init__(self,name,key):
        super().__init__(name)
        self.key=key
        self.isLock=True

    def isLocked(self):
        return self.isLock

    def lock(self):
        self.isLock=True

    def unlock(self,key):
        if key==self.key:
            self.isLock=False


    def open(self):
        if not self.isLock:
            self.isOpen=True



# ----------- 27/7/21 --------------------

def binary_to_decimal(b):
    num=0
    high=len(b)-1
    for digit in b:
        d=int(digit)
        to_add=d*(2**high)
        num+=to_add
        high-=1
    return num

# print(binary_to_decimal("011101"))


def genarate_password():
    letters= string.ascii_letters
    special= string.punctuation
    digits= string.digits
    full_str= letters+special+digits
    password=""
    length= len(full_str)
    for i in range(10):
        inedx= int(random.random()*length)
        password+=full_str[inedx]
    return password

# print(genarate_password())


def merge(book_list):
    books={}
    books_list=[]
    for b in book_list:
        book_details= b.split(",")
        book_name= book_details[0]
        edition =book_details[1]
        if book_name in books.keys():
            if edition>books[book_name]:
                books[book_name]=edition
        else:
            books[book_name]=edition

    for name, edit in books:
        books_list.append(name+","+edit)


class BookOrder():
    def __init__(self, orderID, prod_dict):
        self.orderID=orderID
        self.prod_dict= prod_dict

    def __repr__(self):
        return f"Order # {self.orderID}: [ {self.helper()} ]"

    def helper(self):
        to_return=""
        for name, num in self.prod_dict:
            to_return+=name+" "+"("+num+") "
        return to_return

    def clac_cost(self, product_prices):
        sum=0
        for name, num in self.prod_dict:
            sum+=(num*product_prices[name])
        return sum


class MemberBookOrder(BookOrder):
    def __init__(self,order_id,products_dict,member_type):
        super().__init__(order_id,products_dict)
        self.memberType=member_type

    def __repr__(self):
        # f"{self.memberType} {super().__repr__()}"
        return self.memberType+" "+super().__repr__()

    def clac_cost(self, product_prices):
        sum = super().clac_cost(product_prices)
        if self.memberType == "Gold":
            return sum*0.83
        elif self.memberType == "Silver":
            return sum*0.9
        else:
            return sum


# ------------ 21/2/22----------------

class Item():
    def __init__(self, name,id, volume):
        self.name=name
        self.id=id
        if volume<0:
            raise ValueError("volume must be positive!")
        else:
            self.volume=volume

    def getName(self):
        return self.name

    def getVolume(self):
        return self.volume

    def getID(self):
        return self.id

    def setVolume(self,x,y,z):
        if x>0 and y>0 and z>0:
            self.volume=x*y*z
            print("volume changed!")


class Truck():
    def __init__(self, num, driver,capa):
        self.id=num
        self.driver=driver
        self.capacity=capa
        self.itemList=[]

    def load(self, it):
        if it.getVolume()<=self.capacity:
            self.itemList.append(it)
            self.capacity-=it.getVolume
            return True
        else:
            return False

    def dispatch(self,it):
        if it in self.itemList:
            self.itemList.remove(it)
            self.capacity+=it.getVolume()
            return True
        else:
            return False

class PickupTruck(Truck):
    def __init__(self,num,driver,capa):
        super().__init__(num,driver,capa)
        self.capacity/=2


def orderTrucks(items,avg):  # [it-12 it-54 it-32] 20  , capa= 98 98/20= 4.9
    sum=0
    for it in items:
        sum+=it.getVolume()
    return round(sum/avg)

def loadTrucks(items:list, trucks):
    items.sort(key=lambda x: x._volume) # not necessary but improve the answer
    numT=0
    while len(items)>0:
        if (trucks[numT].capacity>=items[0].getVoulume()):
            trucks[numT].load(items[0])
            items.pop(0)
        else:
            numT+=1


# f= open("bdika.txt","r")
# f.read() # -> all the text as a big string
# f.readline() # -> only 1 line
# f.readlines() # -> list of strings of the lines
# f.close()
# f= open("bdika.txt","w")
# # f= open("bdika.txt","a")
# f.write("asdfghj")
# f.close()
# with open("asdf.txt", "w") as my_file:
#     f.write("asdfghj")
#     f.write("asdfghj")
# # auto closed

f= open("bdika.txt","r")
x= f.readlines()
print(x[4])
f.close()
before= "abcde\n"
before.strip("\n")
print(before)
splited_line= x[4].split(",")
print(splited_line[2])

def isPrime__(n,i):
    if i==2:
        return not n%i==0
    else:
        return isPrime__(n,i-1) and not n%i==0

def isPrime(n):
    isPrime__(n,n-1)

def isPalindrome(my_str):
    if len(my_str)<2:
        return True
    return my_str[0]==my_str[-1] and isPalindrome(my_str[1:len(my_str)-1])

# 123456 -> %10 = 6
# 123456 -> //10 = 12345
# num -> str

# 3245663

def cut_middle(n):
    backup=n
    counter=0
    while backup>0:
        counter+=1
        backup=backup//10
    # counter -> how many digits in my number


























