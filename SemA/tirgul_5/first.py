# # # --------------- list : ----------------------------
# mylist= [1, 3 ,5 ,7 ,9 ,11]
# print(mylist)
# mylist.append([2,0])
# print(mylist)
# mylist[0]=2
# print(mylist)
# mylist.insert(2,8)
# print(mylist)
# mylist.extend([99,999,9999])
# print(mylist)
# # mylist.sort()
# print(mylist)
# mylist.reverse()
# print(mylist)
# mylist.pop()
# print(mylist)
# mylist.index(7)
# print(mylist)
# mylist.remove(9999)
# print(mylist)
# mylist2=["A","b", "c", "d","e"]
# mylist3= mylist+mylist2
# print(mylist3)
# mylist2.clear()
# print(mylist2)
# # # --------------- Tuple : ----------------------------
mytup=(7,6,5,3,1,1,1,1,1)
print(mytup)
print(mytup[2])
print(mytup.index(6))
print(mytup.count(1))
# # # mytup[0]=44
print(len(mytup))
for num in mytup:
    print(num, end=" ")
# #     # print()
# # # print()
# print(mytup[0:6:2])
# tuptup= (10,20,30)
# a, b, c = tuptup
# print(a, b ,c)
# print(mytup+tuptup)
# print(tuptup*3)
# # ----- קומבינה
# tup_list= list(tuptup)
# print(tup_list)
# tup_list.append(10)
# # # # --------------- Dictionary : ----------------------------
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
# print(our_dict.keys())
# print(our_dict.values())
# z= dict_list.popitem()
# z2=our_dict.pop("Ohad")
# print(our_dict)
# print(z2)
# print(z)
# print(dict_list)
# print(dict_list.get("hdfjksdhjf,s",88888))
# #
# dict_list["avg"]=85
# dict_list["avg"]=77
# dict_list["avg"]+=1
#
# print("---------------------")
# print(our_dict.items())
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
#
# mylist=[7,2,6,0,1,66]
# for index, value in enumerate(mylist):
#     print(index, "-",value)
#
# -----------------------------------------
my_student={}
name=input("enter your name")
last=input("enter your last name")
age= input("enter your age")
if age.isdigit():
    age=int(age)
else: raise Exception
my_student["name"]=name
my_student["last"]=last
my_student["age"]=age
# grades={"Python":0,"Infi":0,"Linera Math":0,"Physics":0,"hr":0}
# my_student["grades"]=grades
# for course in my_student[grades.keys()]:
#     my_student[grades[course]]=int(input("enter ", str(course), " grade"))