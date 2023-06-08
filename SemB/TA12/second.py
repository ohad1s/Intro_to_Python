def q1(s):
    new_str=""
    for i in range(len(s)):
        if s[i] not in s[0:i]+s[i+1:]:
            new_str+=s[i]
    return new_str

# a,b=(10,20)

def q3(my_dict):
    new_dict={}
    for k,v in my_dict.items():
        if type(v)==list:
            for elem in v:
                new_dict[elem]=k
        else:
            new_dict[v]=k
    return new_dict

# print(q3({"a":[1,2,3],"ohad":"b",5:True}))

class Clothing():
    def __init__(self,id,fabric,color,price):
        self.__id=id
        self.__fabric=fabric
        self.__color=color
        self.price=price

class Shirt(Clothing):
    def __init__(self,id,fabric,color,price,size):
        super().__init__(id,fabric,color,price)
        if size not in ["S","M","L","XL","XXL"]:
            raise ValueError("Error")
        self.__size=size

class Pants(Clothing):
    def __init__(self,id,fabric,color,price,length,width):
        super().__init__(id,fabric,color,price)
        self.length=length
        self.width=width


class Cart():
    def __init__(self,name,lst):
        self.name=name
        self.lst=lst
        self.current=len(lst)

    def addToCart(self,c):
        if type(c) in [Pants,Shirt, Book]:
            self.lst.append(c)
            self.current+=1

    def __add__(self,other):
        new_lst=self.lst+other.lst
        return Cart(self.name,new_lst)

    def copy(self):
        return Cart(self.name,self.lst)

class Book():
    def __init__(self,id,name,author,price):
        self.__id=id
        self.__name=name
        self.__author=author
        self.price=price

def getDiscountPrice(product):
    new_price=product.price*0.9
    if type(product) in [Shirt,Pants]:
        new_price-=10
    return new_price

c1=Cart("yossi",["Eggs","Milk"])
c2=Cart("yossi",["Bread"])
c3=c1+c2
print(c3.lst)

c4=c2
c4.name="eli"
print(c2.name)

a=[1,2,3]
b=a.copy()

c5=c2.copy()
print(c5.name)
c5.name="beni"
print(c2.name)

stri="bbfj,whfwbe,j.fewhfwgjlfwr"
my_dict={}
for char in stri:
    my_dict[char]=my_dict.get(char,0)+1
print(my_dict)

