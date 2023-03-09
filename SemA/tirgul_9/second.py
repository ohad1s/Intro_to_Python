# a=int(input("enter a num"))
# b=int(input("enter a num"))
# try:
#     z=a/b
# except ZeroDivisionError:
#     print("You cant divide by zero - z=a")
#     z=a
# except TypeError:
#     print("blaa")
#     z=b
# finally:
#     print(z+10)


# name=input("enter your full name")
# if len(name.split())==1:
#     raise "Enter a Full name"

def check_name(name):
    if not isinstance(name,str):
        raise TypeError
    if len(name.split())==1:
        raise ValueError("enter your full name")
    f, l = name.split()
    return f.upper()+l.lower()


def check_formula(formula):
    calculator=0
    if not isinstance(formula,str):
        raise TypeError
    if len(formula)!=5:
        raise "Formula Length Error"
    calc="+-/*"
    for index,char in enumerate(formula):
        if index%2==0:
            if not char.isdigit():
                raise "Not a digit Error!"
        else:
            if char not in calc:
                raise "Not a Symbol Error!"
    pass


def factorial(n):
    if n<0:
        raise ValueError
    if n==0:
        return 1
    return n*factorial(n-1)

def fibo(n):
    if n<1:
        raise ValueError
    if n==1 or n==2:
        return 1
    return fibo(n-1)+fibo(n-2)

def harmonic(n):
    if n<0:
        raise ValueError
    if n==0:
        raise ZeroDivisionError
    if n==1:
        return 1
    return (1/n)+harmonic(n-1)

def rev_rec(my_str):
    if not isinstance(my_str, str):
        raise TypeError
    if len(my_str)==1:
        return my_str
    return my_str[-1]+rev_rec(my_str[0:-1])

def value_of_digit(number,digit): #solution with string
    number_str = str(number)
    if number_str=="":
        return 0
    last_char = number_str[-1]
    if last_char == str(digit):
        return 1
    return 10 * value_of_digit(number_str[:-1], digit)


def value_of_digit_2(number, digit): # without converting to string
    if number==0 and digit==0:
        return 1
    if number == 0:
        return 0
    if number % 10 == digit:
        return 1
    return 10 * value_of_digit_2(number // 10, digit)

print(value_of_digit_2(585, 5))  # Output: 1
print(value_of_digit_2(342, 4))  # Output: 10
print(value_of_digit_2(572, 5))  # Output: 100
print(value_of_digit_2(1942, 8))  # Output: 0
print(value_of_digit_2(1902, 0))  # Output: 10
print(value_of_digit_2(1920, 0))  # Output: 1
print(value_of_digit_2(0, 1))  # Output: 0
print(value_of_digit_2(0, 0))  # Output: 0














