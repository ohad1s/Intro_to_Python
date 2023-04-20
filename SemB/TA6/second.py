import math


def f1(mystr,myint):
    print(mystr*myint)

f1("a",10)

def f2():
    print("Hello World")

# f2()
print(f2())

def f3():
    return "Ciiiii"

# x=f3()
# print(x)


def f4(a,b,c):
    return a+b+c

# sum=f4(1,2,3)
# print(sum+7)

def f5(x,y):
    print(x*y)

# x=f5(5,10)
# print(x)

def f6(mystr,number,name):
    print(f"my name is{name}")
    print(f"I'm {number} years old")
    print(mystr)

# f6(name="ohad",number=25,mystr="bkabka")

def f7(name, age=21):
    print(name,age)
#
# f7("ohad")

def f8(x,y,z):
    print(f4(x,y,z))
    return f3()

# f8(7,2,1)

def moveCharToLast(my_str,ch):
    new_str=""
    counter=0
    for c in my_str:
        if c!=ch:
            new_str+=c
        else:
            counter+=1
    new_str+=(counter*ch)
    return new_str

print(moveCharToLast("hello", "l"))

def reduce(my_str):
    new_str=""
    for i in range(len(my_str)-1):
        if my_str[i]!=my_str[i+1]:
            new_str+=my_str[i]
    new_str+=my_str[-1]
    return new_str

def isPrime(n):
    if n<=2:
        return True
    for i in range(2,n):
        if n%i==0:
            return False
    return True

def primeMarsane(n):
    if not isPrime(n):
        return False
    x=math.log2(n+1)
    if x%1==0:
        return True
    return False

print(primeMarsane(31))

def q4(n):
    my_list=[]
    sum1=0
    for i in range(1,n+1):
    #     if n%i==0:
    #         my_list.append(i)
    # for i in my_list:
        sum1+=(i**2)
    if math.sqrt(sum1)%1==0:
        return True
    return False


def q7(lst1,lst2):
    new_list=[]
    for i in range(len(lst1)):
        new_list.append(lst1[i])
        new_list.append(lst2[i])
    return new_list

