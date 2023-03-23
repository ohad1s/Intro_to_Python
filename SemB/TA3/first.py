# name= input("enter your name:")
# counter=0
# while name[0].islower():
#     counter+=1
#     name = input("enter your name:")
# # print ("success after" , counter , "inputs")
# print(f"success after {counter} inputs")
# # print("success {} after {} inputs {}".format(counter,1,2))

#7:

# my_str= input("enter your str:")
# s=0
# e=len(my_str)-1
# flag=True
# while (s<e):
#     if my_str[s]!=my_str[e]:
#         print("not palindrome")
#         break
#     s+=1
#     e-=1
# else:
#     print("palindrome")
#
# my_str= input("enter your str:")
# s=0
# e=len(my_str)-1
# flag=True
# while (s<e):
#     if my_str[s]!=my_str[e]:
#         flag=False
#         break
#     s+=1
#     e-=1
# if flag:
#     print("palindrome")
# else:
#     print("not")

# my_list=[]
# sum=0
# num=int(input("enter a number"))
# while num!=0:
#     my_list.append(num)
#     sum+=num
#     num = int(input("enter a number"))
# print(my_list)
# print(sum)

my_str= input("enter your str:")
i=0
space_counter=0
while(i<len(my_str)):
    if my_str[i]==" ":
        space_counter+=1
    i+=1
print("there are  {} spaces".format(space_counter))

num=int(input("enter a number"))
factorial=1
while num>1:
    factorial*=num
    num-=1
print(f"factorial is: {factorial}")

number=int(input("enter a number"))
rev_num=0
while number!=0:
    rev_num*=10
    rev_num+=(number%10)
    number=number//10
print(rev_num)


