def loop_factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f

def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

# print(factorial(6))

def fib(n):
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)

# print(fib(45))

def q2(lst):
    if len(lst)==1:
        return lst[0]
    x=lst[0]
    y=q2(lst[1:])
    if x>y:
        return y
    return x

def q3(n):
    if n<10:
        return 1
    return 1+q3(n//10)
# print(q2([7,2,8,3,5,1,0,3,6,8,99]))
def q4(n):
    if n<10:
        return n
    return (n%10)+q4(n//10)


def q9(s:str):
    s=s.strip(" ")
    s=s.lower()
    if len(s)<=1:
        return True
    if len(s)==2:
        if s[0]==s[1]:
            return True
        else:
            return False
    return s[0]==s[-1] and q9(s[1:-1])


print(q9(" AbcD dc Ba "))
