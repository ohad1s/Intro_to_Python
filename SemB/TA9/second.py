def loop_factorial(n):
    f=1
    for i in range(1,n+1):
        f*=i
    return f


def factorial(n):
    if n==1:
        return 1
    return n*factorial(n-1)

# print(factorial(7))

def fib(n):
    if n<3:
        return 1
    return fib(n-1)+fib(n-2)

def min_of_list(lst):
    if len(lst)==1:
        return lst[0]
    x=lst[0]
    y=min_of_list(lst[1:])
    if x<y:
        return x
    return y

# print(min_of_list([7,2,8,5,3,4]))
def num_of_digits(n): #Q3
    if n<10:
        return 1
    return 1 + num_of_digits(n // 10)

# print(num_of_digits(2048))

def sum_of_digits(n): #Q4
    if n<10:
        return n
    return n % 10 + sum_of_digits(n // 10)

# print(sum_of_digits(2048))

def harmonic(n):
    if n==1:
        return 1
    return 1/n + harmonic(n-1)


def palindrome(s:str):
    s=s.strip(" ")
    s=s.lower()
    if len(s)<=1:
        return True
    if len(s)==2:
        return s[0]==s[1]
    return s[0]==s[-1] and palindrome(s[1:-1])

# print(palindrome(" AbcD dc Ba "))

def reverse(s:str):
    if len(s)==1:
        return s
    return s[-1]+reverse(s[:-1])

print(reverse("hello world"))