# my_list=[1,"ohad",True]
# my_str="ohad"
# # my_str[3]="o"
# one=my_str[1]
# zero=my_list[0]
# my_lst2=my_list+[1,23]
# print("a" in "aba")
# x,y,z= 7,2,3
# print(1 in [x,y,z])
# x=7
# y="ohad"

 #5:
# str1=input("please enter a string")
# str2=input("please enter a string")
# str3=str1[::2]+str2[1::2]
# print(str3)
# print(str[::-1])

 #11:
# year= int(input("enter a year!"))
# if year%4==0 and year%100!=0:
#     print("Ciiiiii")
# else:
#     print("No")
#
#12:
# avg=int(input("enter a avg"))
# psycho=int(input("enter a psycho grade"))
# if avg>=85 or psycho>=600:
#     print("Welcome!")
# else:
#     print("good bye!")

#24:
price=20
sum=int(input("enter how many T-shirts"))
if sum<50:
    last_price=price*sum
elif 50 <= sum <=100:
    last_price= price*50 + (sum-50)*price*0.7
else:
    last_price=sum*price*0.5
print("last price is:", last_price)