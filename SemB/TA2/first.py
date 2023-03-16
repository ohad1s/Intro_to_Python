# my_list=[1,"ohad",True]
# # my_str="ohad"
# # my_str[3]="o"
# # one=my_str[1]
# # my_lst2=my_list+[1,23]
# # print("a" in "aba")
# # x,y,z= 7,2,3
# # print(1 in [x,y,z])

#5:
str1=input("enter first string ")
str2=input("enter second string\n")
str3=str1[0::2]+str2[1::2]
print(str3)

# print("Ohad", end=" ")
# print("Shirazi")
# print("Ciii")

#12:
avg=float(input("please enter your avg"))
psycho=float(input("please enter your psycho"))
if avg>=85 or psycho>=600:
    print("Welcome!")
else:
    print("good bye!")
print("Yes")

#25:
a1=float(input("please enter your age"))
a2=float(input("please enter your age"))
price=45
p1=price
p2=price
if a1>=60:
    p1-=15 # p1=p1-15
elif 18<=a1<=21:
    p1-=10
elif a1<=12:
    p1-=5
if a2>=60:
    p2-=15
elif 18<=a2<=21:
    p2-=10
elif a2<=12:
    p2-=5
sum_price=0
if a1==a2:
    sum_price=p1
else:
    sum_price=p1+p2
print("last price: ", sum_price)