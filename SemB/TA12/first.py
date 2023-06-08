def q1(s):
    new_str=""
    for i in range(len(s)):
        if s[i] not in s[0:i]+s[i+1:]:
            new_str+=s[i]
    return new_str

# print(q1("acba"))

def q2(my_dict:dict):
    new_dict={}
    for k,v in my_dict.items():
        if type(v)==list:
            for elem in v:
                new_dict[elem]=k
        else:
            new_dict[v]=k
    return new_dict

class Clothing():
    def __init__(self,id,fabric,color,price):
        self.__id=id
        self.__fabric=fabric
        self.__color=color
        self.__price=price

    def __copy__(self):
        return Clothing(self.__id,self.__fabric,self.__color,self.__price)


class Shirt(Clothing):
    def __init__(self,id,fabric,color,price,size):
        super().__init__(id,fabric,color,price)
        if size not in ["S","M","L","XL","XXL"]:
            raise ValueError("Error")
        self.size=size

class Pants(Clothing):
    def __init__(self,id,fabric,color,price,length,width):
        super().__init__(id,fabric,color,price)
        self.__length=length
        self.__width=width

class Cart():
    def __init__(self,name):
        self.name=name
        self.lst=[]
        self.current=0

    def addToCart(self,c):
        if type(c)==Clothing:
            self.lst.append(c)
            self.current+=1



my_dict={}
stri="gsdkfwgjklgdklgghrskjf"
for c in stri:
    my_dict[c]=my_dict.get(c,0)+1



