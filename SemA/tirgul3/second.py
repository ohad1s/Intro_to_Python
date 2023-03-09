# mylist=["ohad",12, True,"O","1",1]
# print(mylist[1])
# print(mylist[0:6:2])
# mylist.append("gggg")
# print(mylist)
# mylist.append(["o","b",1,True])
# print(mylist)
# mylist.extend(["4,5",False,"9",9])
# print(mylist)
# print(mylist[7][0::2])
# mylist.insert(3,"shirazi")
# print(mylist)
# mylist[3]="shirazi222"
# print(mylist)
# mylist.pop(4)
# print(mylist)
# mylist.reverse()
# print(mylist)
# mylist.extend("bdika")
# print(mylist)
# mylist2=[7,9,2,5,0,1,23,45,62,12]
# mylist3=["v","d","q","p"]
# mylist2.sort()
# mylist3.sort()
# print(mylist2)
# mystr="ohad shirazi"
# for number in range(10,38):
#     print(number, end="::")
# print()
# for char in mystr:
#     print(char, end="\n")
# print()
# for element in mylist:
#     print(element, end=" \t")
#
# num= int(input("enter a number N"))
# factor=1
# for index in range(1,num+1):
#     factor*=index # >> factor = factor * index
#     print(factor)
# print("factorial is: ", factor)
#
# number2= int(input("enter a number"))
# for i in range(1,number2+1):
#     print("*"*i)
# x=20
# y=10
# while y<x:
#     print(y)
#     print("hello")
#     y+=1
# else:
#     print("end")
#
# number_100= int(input("enter 100:"))
# while number_100!=100:
#     number_100 = int(input("enter 100:"))
# else:
#     print("cii")
x=int(input("num"))
while True:
    print(x)
    x=int(input("num"))
    if x==100:
        break

mystr="abcdefghi@gmail.com"
nickname=""
for char in mystr:
    if char=="@":
        break
    nickname+=char
print(nickname)

for i in mystr:
    if i=="@":
        continue
    print(i, end=" ")


mylist=[9,1,5,8,3,8,0,3,9,8]
length=len(mylist)
start=0
end=-1
for i in range(0,length//2+1):
    if mylist[start]!=mylist[end]:
        print("no")
        break
    start+=1
    end-=1
    if i==(length//2):
        print("yes")
# print("yes")


