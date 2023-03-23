# כתבו קטע קוד הקולט מהמשתמש את שמו
# עד שיוקלד נכון - עם אות גדולה-
# נספור כמה פעמים ניסה עד שהצליח

# name= input("enter your name")
# counter=0
# while name[0].islower():
#     counter+=1
#     name = input("enter your name")
# print("success after" ,counter,  "times")
# print(f"success after {counter} times")
# print("success {} {} after {} times".format(1,2,counter))

# כתבו קטע קוד הקולט מהמשתמש מספרים
# כל מספר מכניס לרשימה עד שהמשתמש יזין 0 אותו
# לא נכניס לרשימה אלא נעצור
# את הקליטה ונדפיס את סכום הרשימה

# num= int(input("please enter a number"))
# lst=[]
# sum=0
# while num !=0:
#     lst.append(num)
#     sum+=num # sum = sum + num
#     num = int(input("please enter a number"))
# print(sum)

# כתבו קטע קוד המקבל כקלט מהמשתמש
# מחרוזת וסופר כמה רווחים היא מכילה
# my_str= input("enter your str")
# counter=0
# indx=0
# while indx<len(my_str):
#     if my_str[indx]==" ":
#         counter+=1
#     indx+=1
# print(counter)

#-------------------------------------
#כתבו קטע קוד המקבל מספר
# N ומחשב את העצרת שלו N!

# num= int(input("enter a number"))
# factorial=1
# x=1
# while (x<=num):
#     factorial*=x
#     x+=1
# print(factorial)

# קבלו קטע קוד המקבל כקלט מהמשתמש
# מספר ומחזיר את ההיפוך שלו

# 72  3 --> 327
# %10 ---> אחדות
# # //10 -> ללא אחדות
#
# number= int (input("enter a number"))
# rev=0
# while number>0:
#     rev*=10
#     rev+= number%10
#     number=number//10
# print(rev)

# כתבו קטע קוד הבודק האם מחרוזת שנקלטה מהמשתמש היא פלינדרום
# my_str= input("enter a str")
# s=0
# e=len(my_str)-1
# while s<e:
#    if my_str[s]!=my_str[e]:
#       print("not palinrome")
#       break
#    s+=1
#    e-=1
# else:
#    print("palindrome")

my_str= input("enter a str")
s=0
e=len(my_str)-1
flag=True
while s<e:
   if my_str[s]!=my_str[e]:
      flag= False
      break
   s+=1
   e-=1
if flag:
   print("Palindrome")
else:
   print("Not palindrome")

