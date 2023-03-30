# import random
#
# for i in range(10):
#     print(i)
# list1=["yossi", "dani",5,"Kobi",True]
#
# for elem in list1:
#     print(elem)
#
# my_str="fgadsklfw"
#
# for char in my_str:
#     print(char)
#
# num= 87349
#
# # for digit in num:
# # num[0]
#
# num2=int(input("enter a number"))
#
# for i in range(1,num2+1):
#     print(((num2-i)*" ")+("*"*i))
#
#
# #5:
# num=int(input("enter a N"))
# lst=[]
# for i in range(num):
#     x=random.randint(0,num)
#     if x%3==0:
#         print(x)
#     lst.append(x)
#
# #6:
# maxi=0
# num=int(input("enter a N"))
# for i in range(num):
#     x=int(input("enter a Number"))
#     if i==0:
#         maxi=x
#     else:
#         if x>maxi:
#             maxi=x
#
#
# #6:
# lst=[]
# num=int(input("enter a N"))
# for i in range(num):
#     x=int(input("enter a Number"))
#     lst.append(x)
# print(max(lst))
#
# #8:
# num=int(input("enter a N"))
# for i in range(2,num):
#     if num%i==0:
#         print("not prime")
#         break
# else:
#     print("prime")
#
# my_tup=(0,1,5)
# x=my_tup[1]
# # my_tup[2]=3

my_set={1,6,3,15,8,1,1,1,1}
print(my_set)
for s in my_set:
    print(s)

# for i in range(1,10):
#     for j in range(1,10):

for hour in range(0,24):
    for min in range(0,60):
        if hour<10 and min<10:
            print(f"0{hour}:0{min}")
        elif hour<10:
            print(f"0{hour}:{min}")
        elif min<10:
            print(f"{hour}:0{min}")
        else:
            print(f"{hour}:{min}")
