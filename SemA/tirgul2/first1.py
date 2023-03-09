# x="hello world"
# y= "bye bye"
# z= x+y
# t= x[4]
# q= y[-1]
# d=x[2:2:9]
# x=5
# names_str= "ohad,yoshasi,dhani"
# names=names_str.split("ah")
# print(names)
# tt=names_str.index("a")
# print(tt)
# zz="45"
# zz2="abc"
# print(zz.isdigit())
# print(zz2.isdigit())
# user_num=input("enter a number")
# print("is digit>? : " , user_num.isdigit())
#
# ----------
# 5==7
# 5==5
# True and True
# False and False
# True and False
# False or True
# print(5==5 or 2==3 and (4!=2))
# mylist=[]
# mylist2=["ohad",25,"shirazi",True]
# len(mylist)
# print(mylist2[0:3:2])
# mylist2.insert(2,"5")
# -----------------
# avg=input("please enter your avg grades")
# psycho = input("please enter your psycho grade")
# if avg.isdigit() and psycho.isdigit():
#     avg=int(avg)
#     psycho=int(psycho)
#     if (avg>=85 or psycho>=600):
#         print("Welcome!")
#     else:
#         print("Go Home...")
# else:
#     print("Error!")
#
# nickname=input("enter your noickname")
# x="#"
# if "@" in nickname:
#     print("True")
# else:
#     print("NO")
#
# if x in nickname:
#     print("###")

# price= float(input("enter price"))
# leg= round(price)
# cus= int(price)
# cus2= price//1

# price= 20
amount= int(input("please enter amount"))
if amount<=50:
    print("price is: " , amount*20 )
elif amount>50 and amount<101:
    print("price is: ", 50*20+(amount-50)*0.7*20)
else:
    print("price is: ", amount*20*0.5)



