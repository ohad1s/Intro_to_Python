# a=int(input("enter a num"))
# b=int(input("enter a num"))
# try:
#     z=a/b
# except ZeroDivisionError:
#     print("You cant divide by zero - z=a")
#     z=a
# finally:
#     print(z)

# my_name= input("enter your full name")
# if len(my_name.split())==1:
#     raise "its not a full name"
    # raise ZeroDivisionError ("ddhksdgf")
# if my_name.isdigit():
#     raise ValueError

# f= open("myfile.txt", "w")
#       "same":
# with open("myfile.txt", "w+") as f:
#     f.write("fdsf")

def check_name(name):
    if not isinstance(name,str):
        raise TypeError ("enter a valid name")
    if len(name.split())==1:
        raise ValueError ("enter a full name")
    first, last = name.split()
    return first.title()+" "+last.title()

# print(check_name("3453"))

def check_formula(formula):
    if len(formula)!=5:
        raise "Length Formula Error"
    for index, char in enumerate(formula):
        calc="+-/*"
        if index%2==0:
            if not char.isdigit():
                raise "Length Formula Error"
        else:
            if char not in calc:
                raise "Length Formula Error"
        return None
    # continioue at home

def factorial(n):
    if n<0:
        raise ValueError
    if n==0:
        return 1
    return factorial(n-1)*n

def fibo(n):
    if n<0:
        raise ValueError
    if n==0:
        return 0
    if n==1:
        return 1
    return fibo(n-1)+fibo(n-2)

# print(fibo(50))

def harmonic(n):
    if n<0:
        raise ValueError
    if n==0:
        raise ZeroDivisionError
    if n==1:
        return 1
    return (1/n)+harmonic(n-1)

# x=harmonic(500)
# print(x)

def rec_rev(my_str):
    if len(my_str)==1:
        return my_str
    return my_str[-1]+rec_rev(my_str[0:-1])

print(rec_rev("Hello"))




