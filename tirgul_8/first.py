import random

# myfamily=["Ohad","Michael","Shaked","Mika","Guetta","Ido"]
# myfile= open("class.txt","w")
# for name in myfamily:
#     myfile.write(name)
#     myfile.write("\n")
# myfile= open("class.txt", "r")
# file_list=myfile.readlines()
# print(file_list)
# line= myfile.readline()
# print(line)
# line=myfile.readline()
# print(line)
# myfile= open("class.txt", "a")
# myfile.write("Neta")
# myfile= open("blabla.txt", "r+")
# for i in range(200):
#     myInt=str(random.randint(1,1000))
#     myfile.write(myInt)
#     myfile.write("\n")
# for i in range(1,200):
#     line=myfile.readline()
#     if i==12:
#         print(line)
# lines=myfile.readlines()
# print(lines[11])
# myfile=open("myfile10.txt")
# myfile=open("myfile200.txt","r") //Error

def Avg_nums_from_file(file_name):
    f= open(file_name,"r")
    lines= f.readlines()
    counter=0
    for line in lines:
        counter+=int(line)
    return counter/len(lines)

# avg_file=Avg_nums_from_file("blabla.txt")
# print(avg_file)
# function without return
def map_square(mylist):
    for i in range(len(mylist)):
        mylist[i]=mylist[i]**2


# lst1=[2,4,6]
# print(lst1)
# map_square(lst1)
# print(lst1)

#barbie.txt

f= open("Barbie.txt","r")
lines=f.readlines()
barbie_prices={}
for i in range(1,len(lines)):
    name,price =lines[i].split("    ")
    price=price.rstrip("\n")
    barbie_prices[name]=int(price)

print(barbie_prices)

# def mul_vec(vec,scalar):
#     mul_scalar=[]
#     for i in range(0,len(vec)):
#         mul_scalar.append(vec[i]*scalar)
#     return mul_scalar
# vec=input("wefefewr").split(" ")
#
# x= mul_vec(vec,2)
# print(x)




