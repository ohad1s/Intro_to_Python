x=77
mylist=["both", 45, True,x,"ohad" ]
print(mylist[-1])
mylist.index(45)
mylist.append("ohad2")
print(mylist)
mylist.extend(["ohad", "cii","shirazi"])
print(mylist)
mylist.append([1,2,3])
print(mylist)
mylist.pop()
mylist.insert(2,"999")
print(mylist)
mylist.pop(2)
print(mylist)
# mylist.sort()
# print(mylist)
mylist.remove("ohad")
print(mylist)
mylist.reverse()
print(mylist)

for i in range(0,101,5):
    print(i, end=" ")
print(" ")
for element in mylist:
    print(element, end=" ")
mylist2= [1,2,3,4,5,6,7]
print()
for elem in mylist2:
    print(elem*5)
mystr="ohad shirazi"
mylststr=mystr.split(" ")
for char in mylststr:
    print("hello "+char)
#
# mynumber= int(input("enter a number"))
# sum=0
# for i in range(1,mynumber+1):
#     sum+=i # sum=sum+i
# print(sum)
# counter=0
# while counter<15:
#     print("hello ", counter)
# counter+=1

# i=0
# sum=0
# while i<=mynumber:
#     sum+=i # sum=sum+i
#     i+=1
# print(sum)

# number_100= int(input("enter 100"))
# while number_100!=100:
#     number_100 = int(input("enter again"))
# else:
#     print("ciiii")
#
# while True:
#     number_100 = int(input("enter again"))
#     if number_100==100:
#         break
# mystr2="blla@gmam"
# nickname=""
# for char in mystr2:
#     if char=="@":
#         continue
#     print(char)
#     print("ciiiii")


print("a")
print("*********************")
print("b")
print("*********************")
print("C")
print("*********************")







