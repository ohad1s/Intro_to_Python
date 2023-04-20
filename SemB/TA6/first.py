import math


def f1(mystr,myint):
    print(mystr*myint)

# f1("a",10)

def f2():
    print("Hello World")

# f2()

def f3():
    return "Ciiiii"

# x=f3()


def f4(a,b,c):
    return a+b+c

# d=f4(1,2,3)

def f5(x,y):
    print(x*y)

# x=f5(5,10)
# print(x)

def f6(mystr,number,name):
    print(f"my name is{name}")
    print(f"I'm {number} years old")
    print(mystr)

f6(name="ohad",number=25,mystr="bkabka")

def f7(name, age=1):
    print(name,age)
#
# f7("ohad")

def f8(x,y,z):
    print(f4(x,y,z))
    return f3()
# f8()


def moveCharToLast(char,mystr):
    counter=0
    newstr=""
    for c in mystr:
        if c==char:
            counter+=1
        else:
            newstr+=c
    newstr+=(counter*char)
    return newstr

res= moveCharToLast("l","hello")
print(res)


def reduce(mystr):
    newstr=""
    for i in range(len(mystr)-1):
        if mystr[i]!=mystr[i+1]:
            newstr+=mystr[i]
    newstr+=mystr[-1]
    return newstr

# print(reduce("xxxxaaabbyyyyt"))

def reduce2(mystr):
    newstr=mystr[0]
    for i in range(1,len(mystr)):
        if mystr[i]!=newstr[-1]:
            newstr+=mystr[i]
    return newstr

print(reduce("xxxxaaabbyyyy"))


def isPrime(x):
    pass

def marsanePrime(x):
    if not isPrime(x):
        return False
    for i in range(1,int(math.sqrt(x))):
        if 2**i == x+1:
            return True
    return False

