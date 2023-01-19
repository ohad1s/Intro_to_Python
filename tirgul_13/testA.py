import math


def draw_seq(ch,n):
    print(n*ch)
    for i in range(n-2):
        print(ch+(""*(n-2))+ch)
    print(n*ch)

def maxNum(my_str):
    maxi=0
    max_local=0
    for ch in my_str:
        if ch.isdigit():
            max_local=max_local*10 + int(ch)
        else:
            if max_local>maxi:
                maxi=max_local
            max_local=0
    return maxi


# print(maxNum("kgdasjk23fdskjfhkj65bdskjfbdsjfkb874SFDKSDHxf,j5s"))


def factorial(n):
    f=1
    for i in range(1,n+1):
        f=f*i
    return f

def factorial_rec(n):
    if n==1:
        return 1
    return n*factorial_rec(n-1)


def my_sin(x,accuracy):
    sin=0
    p=1
    n=3
    local_calc= ((x**p)/factorial(p))-((x**n)/factorial(n))
    while accuracy < local_calc:
        sin+=local_calc
        p+=4
        n+=4
        local_calc = ((x ** p) / factorial(p)) - ((x ** n) / factorial(n))
    return sin

# print(my_sin(math.pi/2,0.00000000000000003))

def pascal(n):
    tri=[[1],[1,1]]
    for i in range(n-2):
        lst=[1]
        for j in range(len(tri[-1])-1):
            to_add= tri[-1][j]+tri[-1][j+1]
            lst.append(to_add)
        lst.append(1)
        tri.append(lst)

    for line in tri:
        for num in line:
            print(num, end=" ")
        print()


pascal(8)