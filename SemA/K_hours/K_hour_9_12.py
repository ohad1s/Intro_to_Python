my_dict={}
my_dict["mykey"]="myvalue"
my_dict["mykey"]=5
my_dict["mykey"]+=1
print(my_dict)
print(my_dict.items())
print("----------------")

def myName(name): #קלט של פוקציה
    msg="Hello "+name
    return msg #פלט של פונקציה

# my_msg= myName("Ohad")
# print(my_msg)

nickname= input("enter your name")
my_msg= myName(nickname)
print(my_msg)

print("-------------------")

def isPrime(number):
    for i in range(2,number):
        if number%i==0:
            return False
    return True

# fibonachi: 0 1| 1 2 3 5 8 13 21 ...
#            1 2| 3 4 5 6 7  8  9....

def fibo(n):
    first=0
    second=1
    if n==1:
        return first
    if n==2:
        return second
    for i in range(3,n):
        helper=first
        first=second
        second=second+helper
    return first+second

n_9=fibo(9)
n_8=fibo(8)
n_23=fibo(23)
n_3=fibo(3)
print(n_3, n_8, n_9, n_23)

def Common_pvt_Name():
    names_list=[]
    for i in range(0,30):
        name= input("enter your name")
        names_list.append(name)
    my_dict_names={}
    for n in names_list:
        first_name,family_name=n.split(" ")
        if first_name in my_dict_names.keys():
            my_dict_names[first_name]+=1
        else:
            my_dict_names[first_name]=1
    common_name=[]
    max_app=0
    for pvt_name, counter in my_dict_names.items():
        if counter>max_app:
            common_name.clear()
            max_app=counter
            common_name.append(pvt_name)
        elif counter==max_app:
            common_name.append(pvt_name)
    return common_name

import math
def sum_square_number(number):
    square_sum_counter=0
    for i in range(1,number+1):
        if number%i==0:
            i_square=i**2
            square_sum_counter+=i_square
    sqrt_counter=math.sqrt(square_sum_counter)
    sqrt_counter=sqrt_counter//1
    if sqrt_counter**2==square_sum_counter:
        return True
    else:
        return False














