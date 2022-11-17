# mystr=input("enter a string")
# mychar=input("enter a char")
# counter=0
# for char in mystr:
#     if char==mychar:
#         counter+=1
# print(counter)
# -----------------------------
# number= int(input("enter a num"))
# for i in range(1,number+1):
#     print(i*10)
# -----------------------------
# num= int(input("enter a num to check"))
# mylist=[]
# while num != 0:
#     mylist.append(num)
#     num = int(input("enter a num to check"))
# print(mylist)
# -------------------------
# num= int(input("enter a number"))
# isPrime=True
# for i in range(2,num):
#     if num%i==0:
#         isPrime=False
#         break
# print("is prime: ", isPrime)
# ---------------------------------
# flag=False
# for i in range(1,11):
#     if i==10:
#         flag=True
#     if flag:
#         print(i)
#     else:
#         print(i, end=",")
# ------------------------------
# num= input("enter a num")
# if not num.isdigit():
#     print("TRY AGAIN")
# else:
# ------------------------------
num= int(input("enter a num"))
for i in range(1,num+1):
    if i%6==0 or "7" in str(i):
        print("boom")
    else:
        print(i)
