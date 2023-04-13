# my_l=[1,7,2,8,9,3,4]
# for i in range(len(my_l)):
#     if my_l[i]%2==0:
#         print(i, my_l[i])

#
# for tup in enumerate(my_l):
#     print(tup)
#
# x, y = (10,20)
#
# for index,elem in enumerate(my_l):
#     if elem%2==0:
#         print(index, elem)
#
# l1=[3,2,1,9,0,4]
# l2="abc"
# l3=44
# l4= [6,7,9]
# l5= "ytr"
#
# z_1= zip(l1,l2,l4,l5)
# for z in z_1:
#     print(z)

# my_zip=[]
# for i in range(min(len(l1),len(l5))):
#     my_zip.append((l1[i],l5[i]))
#
# print(my_zip)

# my_dict={"ohad":7,"yossi":20,5:20, "p":[1,2,3],7:{"p":0}}
# print(my_dict["ohad"])
# my_dict["yossi"]=30
# print(my_dict["yossi"])
# my_dict.pop("yossi")
# my_dict["dani"]=30
# my_dict.get(9,"9999")
#
# for elem in my_dict:
#     print(elem)
#
# for v in my_dict.values():
#     print(v)
#
# for tup in my_dict.items():
#     print(tup)
#
# for k,v in my_dict.items():
#     print(k,v)
# #1+2:
# my_list=[]
# inp=int(input("enter a number"))
# while inp!=0:
#     my_list.append(inp)
#     inp = int(input("enter a number"))
# my_d={}
# for index, elem in enumerate(my_list):
#     if elem%2!=0:
#         my_d[index]=elem
# # 3+4:
# mid= len(my_list)//2
# l1=my_list[0:mid]
# l2=my_list[mid:len(my_list)]
# print(l1)
# print(l2)
#
# mul=[]
# for i,j in zip(l1,l2):
#     mul.append(i*j)

# a=1
# b=a
# b+=1
# print(a)
# print(b)

# la=[1,2,3]
# lb=la
# lb[0]=7
# print(la)
# print(lb)


la=[1,2,3]
lb=la.copy()
lb[0]=7
print(la)
print(lb)







