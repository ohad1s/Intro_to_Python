mystr=input("enter a string")
str_length_half=len(mystr)//2
for i in range(0,str_length_half):
    j=len(mystr)-1-i
    if mystr[i]!=mystr[j]:
        print("No")
        break
    if i==str_length_half-1:
        print("Yes")
# ------------------------------------
# Flag=True
# for i in range(0,str_length_half):
#     j=len(mystr)-1-i
#     if mystr[i]!=mystr[j]:
#         Flag=False
#         break
# if Flag:
#     print("YES")
# else:
#     print("NO")
# print("YES")

# ------------------------------------
# mystr=input("enter a string")
# str_length_half=len(mystr)//2
#
# left_side=0
# right_side=len(mystr)-1
# while left_side<right_side:
#     if mystr[left_side]!=mystr[right_side]:
#         print("NO")
#         break
#     left_side+=1 # left_side=left_side+1
#     right_side-=1
# else:
#     print("Yes")
# ------------------------------------
# mystr=input("enter a string")
# counter=0
# for letter in mystr:
#     if letter==mystr[0]:
#         counter+=1 # counter= counter +1
# print(counter)
# ------------------------------------
# number=int(input("enter a number"))
# mylist=[]
# while 10 < number < 70:
#     mylist.append(number)
#     number = int(input("enter a number"))
# print(mylist)
# -------------------------------
# for hour in range(0,24):
#     for min in range(0,60):
#         print(str(hour)+":"+str(min))

# mylist=[1,2,7,3,9,43,0,2,7,8,23,76,43,56,12]
# # mylist.sort()
# for i in range(len(mylist)):
#     for j in range(i,len(mylist)):
#         if mylist[i]>mylist[j]:
#             mylist[i], mylist[j] = mylist[j], mylist[i]
# print(mylist)

