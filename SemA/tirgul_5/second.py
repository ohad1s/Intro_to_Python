# # # # --------------- list : ----------------------------
# # mylist= [1, 3 ,5 ,7 ,9 ,11]
# # print(mylist)
# # mylist.append([2,0])
# # print(mylist)
# # mylist[0]=2
# # print(mylist)
# # mylist.insert(2,8)
# # print(mylist)
# # mylist.extend([99,999,9999])
# # print(mylist)
# # # mylist.sort()
# # print(mylist)
# # mylist.reverse()
# # print(mylist)
# # mylist.pop()
# # print(mylist)
# # mylist.index(7)
# # print(mylist)
# # mylist.remove(9999)
# # print(mylist)
# # mylist2=["A","b", "c", "d","e"]
# # mylist3= mylist+mylist2
# # print(mylist3)
# # mylist2.clear()
# # print(mylist2)
# # # # --------------- Tuple : ----------------------------
# mytup=(7,6,5,3,1,1,1,1,1)
# print(mytup)
# print(mytup[2])
# print(mytup.index(6))
# print(mytup.count(1))
# # # # mytup[0]=44
# print(len(mytup))
# for num in mytup:
#     print(num, end=", ")
# print()
# # # # print()
# print(mytup[0:6:2])
# tuptup= (10,20,30)
# mylist=[10,11,12]
# x,y,z=mylist
# print(x,y,z)
# a, b, c = tuptup
# print(a, b ,c)
# tuptup2=(a,x,c)
# print(mytup+tuptup)
# print(tuptup*3)
# # # ----- קומבינה
# # tup_list= list(tuptup)
# # print(tup_list)
# # tup_list.append(10)
# # # # # --------------- Dictionary : ----------------------------
# my_dict={}
# studentA={"name":"ploni", "last":"almoni", "age": 25}
# numbers= {0:7, 2:8, 9:2}
# letters={"a":7, "b":0,"c":12}
# mix={"a":20,45:"132123",True:[1,2,3],(1,2,3):{"ohad":2}}
# bools={"ohad":True, "dan":False, "yossi":True}
# dict_list={"ohad":[1,2,3], "Dan":[4,5,6], "Yossi": (1,2,3)}
# dict_free= {True:"ohad", 5:[1,2], "ohad":"opop"}
# our_dict={3:4,"FCB":"6-2","MHFC":"2-0","MASCARA":"BLACK",(1,2,3):True}
# print(studentA["name"])
# print(letters["c"])
# yossi="c"
# print(letters[yossi])
# print(our_dict)
# our_dict["Ohad"]=25
# print(our_dict)
# our_dict["Ohad"]=17
# print(our_dict)
# my_dict2={"ohad":7,"ohad":8}
# print(my_dict2)
# print(our_dict.keys())
# print(our_dict.values())
# print(our_dict.items())
# z= dict_list.popitem()
# z2=our_dict.pop("Ohad")
# print(our_dict)
# print(z2)
# print(z)
# print(dict_list)
# print(dict_list.get("hdfjksdhjf,s"))
# # #
# dict_list["avg"]=85
# dict_list["avg"]=77
# dict_list["avg"]+=1
# #
# # print("---------------------")
# # print(our_dict.items())
# print("---------------------")
# for key, value in our_dict.items():
#     print(key, value)
# print("---------------------")
# for tup in our_dict.items():
#     print(tup)
# print("---------------------")
# for key in our_dict.keys():
#     print(key)
# print("---------------------")
# for val in our_dict.values():
#     print(val)
# print("---------------------")
# for i in our_dict:
#     print(i)
# print("-----------------")
# mylist=[7,2,6,0,1,66]
# for index, value in enumerate(mylist):
#     print(index, "-----",value)
#
# mystr=input("enter a string")
# counter_dict={}
# for char in mystr:
#     if counter_dict.get(char)==None:
#         counter_dict[char]=1
#     else:
#         counter_dict[char]+=1
# print(counter_dict)
# =---------------------
# tuplist=[(1,2),(3,4),(9,0)]
# for key ,val in tuplist:
#     print(key,val)

my_class={"s1":{},"s2":{},"s3":{},"s4":{},"s5":{}}
for key,value in my_class.items():
    my_class[key]["name"]=input("enter your name")
    my_class[key]["id"]=input("enter your id")
    my_class[key]["grades"]={"Algebra":0,"Infi":0,"Python":0}
    for course,grade in my_class[key]["grades"].items():
        my_class[key]["grades"][course]=input("enter grade")
print(my_class)

