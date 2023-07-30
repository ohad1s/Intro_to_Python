# int -> -7 , 0 ,8 ...
# str -> "ohad" , "5" "True", "-3", "bukjsefgkew"
# float -> 0.5 , 0.2 -0.3
# bool -> True, False

print("Hello","World")
my_str="5"
my_str2="2"
my_str3=my_str+my_str2
print(my_str3)
my_str4= "!"*10
print(my_str4)
# + - * / ** // %
print(5/2)
print(5//2)
print(5%2)

# and or not
# <= >= < >
# == !=
print(2==2)
print(3!=3)
print(3!=2 and 2==1)
print(not (3<4 or 5<2))


print(len("oh ad"))
# len(768) -> Error!
my_str5= "Hello World!"
x=my_str5[0]
# str[x:y:z] (start, end(not include), step)
x2=my_str5[1:7:2]
# "oh fkhdgf kcx"
# [2:8:2]
# fhg
x=5723
y="ohad"
z=y[1]
q=y[3]
zq= z+q
o=y[0]*10
# o2= y[0]+2 -> Error!

# print(not 3==5) -> True


#
# my_name= input("please enter your name")
# print(my_name)
# # #
# fam_name= input("please enter your last name")
# print("Hello "+ my_name+" "+fam_name)
#
x1="ohad"
x2="5"
x3="True"
y=5
z=8.3
b=True
#
x4=int(x2)
x5= str(342)

# print(int(b))
# print(bool(-5))
#

#
# num1 = float(input("enter first num"))
# num2 = float(input("enter second num"))
# num3 = float(input("enter third number"))
# avg = (num1 + num2 + num3) / 3
# print("your avg is: ", avg)
#
# c_temp= float(input("enter your c temp"))
# f_temp= c_temp*9/5 +32
# print("your f temp is: ",f_temp)
#
t=type(x)
print(t)
t2=type(x2)
print(t==t2)
#
# print(type(x))
booli= isinstance("ohad",str)
print(booli)
# x="ohad"
# q = x[1]
# print(q)
#
number1=472384
print(number1[3]+"\n"+"aew")