def div_numbers(a,b):
    try:
        res=  a/b
    except ZeroDivisionError:
        print("can divide by zero")
    finally:
        print("finally")

# x=div_numbers(2,0)
# print("hello")




def mul_str(name,number):
    if type(name)!=str or type(number)!=int:
        raise TypeError("name must be a string and number must be an integer")
    for i in range(number):
        print(name)

def buy_beer(name,age):
    if age<18:
        raise ValueError("call the manager")
    print(f"hello {name}")

# mul_str("ohad",0)

def rot(direction ,n,string):
    if type(n)!=int or type(string)!=str or type(direction)!=str:
        raise TypeError("....")
    if direction not in ["right","left"] or n<0:
        raise ValueError("...")
    # rest of code

