# for i in range(900):
#     print("hello")
#
# sum=0
# n=int(input("enter a num"))
# for i in range(1,n+1):
#     sum+=i
#
# my_lst=[4,1,8,"fs",True]
#
# for elem in my_lst:
#     print(elem)
#
# my_str="ejkfgefk"
# for char in my_str:
#     print(char)
#
# for i in range(len(my_str)):
#     if my_str[i]=="f":
#         print(i)
#         break
# else:
#     print("not f")
#
# lst=[7,8,2]
# print(lst[0])
# lst[1]=0
# lst.append(5)
#
# my_tuple=(7,8,2,4)
# print(my_tuple[0])
import random

my_set={1,5,2,3,1,2,5,6,1}
# print(my_set)
# for i in my_set:
#     print(i)

lst_set=list(my_set)
print(lst_set)

num=589345

# for i in num:

#3:
# n=int(input("give  me a N"))
# for i in range(1,n+1):
#     print(((n-i)*" ")+(i*"*"))


#6:
# num=int(input("enter a num"))
# list1=[]
# for i in range(num):
#     x=float(input("enter a number"))
#     list1.append(x)
# print(max(list1))


# num=int(input("enter a num"))
# maxi=0
# for i in range(num):
#     x=float(input("enter a number"))
#     if i==0:
#         maxi=x
#     else:
#         if x>maxi:
#             maxi=x
# print(maxi)
#
# n= int(input("enter a number"))
# for i in range(2,n):
#     if n%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")

# for hour in range(0,24):
#     for minute in range(0,60):
#         if hour<10 and minute<10:
#             print(f"0{hour}:0{minute}")
#         elif hour<10:
#             print(f"0{hour}:{minute}")
#         elif minute<10:
#             print(f"{hour}:0{minute}")
#         else:
#             print(f"{hour}:{minute}")

list1=[]
counter_list=[]
for i in range(100):
    x=random.randint(0,99)
    list1.append(x)
    counter_list.append(0)
for number in list1:
    counter_list[number]+=1
print(list1)
print(counter_list)