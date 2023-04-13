# x=10
# if x>0:
#     print("pos")
# elif x==0:
#     print("0")
# else:
#     print("neg")
#
#
# set= {}
#
# for i in range(10):
#     if i<5:
#         print(i)
#         for j in "28947213094":
#             print(i*j)
import copy

my_l=[1,7,2,8,9,3,4]
# for i in range(len(my_l)):
#     if my_l[i]%2==0:
#         print(i, my_l[i])


x,y =(10,20)

# for tup in enumerate(my_l):
#     print(tup)

# for index, elem in enumerate(my_l):
#     print(index,elem)

l1= [6,1,2,3]
l2=["a","b","c"]
# l3=[1,7,9,8]
# l4=[True,False,True]
# myz=zip(l1,l2,l4,l3)
# print(myz)
# for i in myz:
#     print(i)

# my_zip=[]
# for i in range(min(len(l1),len(l2))):
#     my_zip.append((l1[i],l2[i]))
# print(my_zip)
#
# my_d={5:"ssa","ohad":True,"table":[1,2,3],[1]:"yossi",(5):7,"dict":{1:10}}
# # my_d[5]
# my_d[5]="777"
# my_d.get(7,"Yossi")
# my_d.pop(5)
# my_d.get(5,"Yossi")
# my_d[99]=10
#
# print(my_d)
# for pair in my_d:
#     print(pair)
# print(":---------------------")
# for pair in my_d.values():
#     print(pair)
# print(":---------------------")
# for k,v in my_d.items():
#     print(k, v)
# print(":---------------------")
# for tup in my_d.items():
#     print(tup)
#
#
# lst=[]
# inp= int(input("enter a number"))
# while inp!=0:
#     lst.append(inp)
#     inp = int(input("enter a number"))
#
# d={}
# for index, elem in enumerate(lst):
#     if elem%2!=0:
#         d[index]=elem
#
# print(d)
#
# mid = len(lst)//2
# l11= lst[0:mid]
# l22=lst[mid:-1]
# l33=[]
#
# for i,j in zip(l11,l22):
#     l33.append(i*j)
#
# print(l33)
#
# a=[7,3,2,5]
# b=a
# print(b)
# b[0]=9
# print(b)
# print(a)

# a=11
# b=a
# b+=1
# print(b)
# print(a)

lst1=[4,7,8,9]
lst2=copy.deepcopy(lst1)
lst2[0]=10
lst3= lst1.copy()
lst3[0]=99
print(lst1)



