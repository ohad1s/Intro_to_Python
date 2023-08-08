# Today:
# loops of dict/tup/str
# break
# continue
# nested loops
# else for loops
# while loops
# ---------------------------------------
my_str="hello world"
counte=0
for char in my_str:
    print(char)
    print("hello char")
    counte+=1
print("Ciii")
#
my_tup=(1,"A","Ohad",True)
for elem in my_tup:
    print(elem)
#
for counte, c in enumerate(my_str):
    print(counte, ":", c)

my_dict={1:"a",2:"B",3:"C",4:True}
for elem in my_dict:
    print(elem)
print("----------")
for k in my_dict.keys():
    print(k)
print("----------")
for v in my_dict.values():
    print(v)
print("-----with tup-----")
for tup in my_dict.items():
    print(tup)
print("-----without tup-----")
for k,v in my_dict.items():
    print(k,v)
print("-----without tup 2-----")
for k,v in my_dict.items():
    if k<=2:
        print(k)
    else:
        print(v)
#
# for tup in enumerate(my_dict):
#     print(tup)    #### possible but not good
#
char="a"
s= "baksfhsdjkfhsdkfhsdghsdoghsgsflsgfs"
# for c in s:
#     if c==char:
#         print("Yes")
#         break
#     else:
#         print("NO")

# for c in s:
#     if c==char:
#         print("Yes")
#         break
# print("NO")

for c in s:
    if c==char:
        print("char is appear")
        break
else:
    print("char is not appear")

# # -------------------------------------
flag = False
for c in s:
    if c == char:
        flag = True
        break
#
if flag:
    print("yes")
else:
    print("no")
#
lst=[1,2,7,3,9,2,4,6,9,2,1,6,8]
sum_odd=0
for num in lst:
    if num%2==0:
        continue
    print(num)
    sum_odd+=num
#
str_lst=["dog","cat","barbie","insert","pop","Python"]
for elem in str_lst:
    print(elem)
    for char in elem:
        print(char)
    print()
#
for counte in range(1, 11):
    for j in range(1,11):
        print(counte * j, end=" ")
    print()
#
name="ohad"
age=25
print(f"im {name} and im {age} years old")
print("im {} and im {} years old".format(name,age))


for hour in range(24):
    if hour<10:
        hour=f"0{hour}"
    for mint in range(60):
        if mint<10:
            mint=f"0{mint}"
        print(f"{hour}:{mint}")


lst=[]
num= int(input("enter a num"))
while num != 0:
    lst.append(num)
    num = int(input("enter a num"))
print(lst)
#
lst=[3,5,7,2,9,0,1,6,1]
counte=0
sum=0
while lst[counte]%2!=0:
    sum+=lst[counte]
    counte+=1    # i = i +1
#
counte=0
while counte<len(lst):
    if lst[counte]%2==0:
        counte+=1
        continue
    print(lst[counte])
    counte+=1


lst=[]
my_str= input("enter a str")
counter=0
while counter < 100 and my_str!= "stop":
    for char in my_str:
        if char in "abcdefghijklmn":
            lst.append(char)
    counter+=1
    my_str = input("enter a str")
print(lst)

num=int(input("enter a number"))
while num>9:
    sum=0
    while num!=0:
        sum+=num%10
        num=num//10
    num=sum
print(num)

















