# f= open("myfile.txt","w")
# names=["Ohad", "Yuval", "Bnaya","Adir", "Yonatan"]
# for name in names:
#     f.write(name)
#     f.write("\n")
# f= open("myfile.txt","a")
# f.write("Yossi")
# f= open("myfile.txt","r")
# file_string=f.read()
# print(file_string)
# file_list=f.readlines()
# print(file_list)
# line=f.readline()
# print(line)
# line=f.readline()
# print(line)
# lines=f.readlines()
# print(lines)
# f= open("blabla.txt","r")
# lines=f.readlines()
# counter=0
# for number in lines:
#     counter+=int(number)
# avg=counter/len(lines)
# print(avg)
import random

def printHello():
    print("Hello World")

def randomFile(file_name,num):
    f=open(file_name,"a")
    for i in range(num):
        x= random.randint(1,num)
        f.write(str(x))
        f.write("\n")
    f.close()

# randomFile("numbers2.txt",100)

# printHello()
# nums=open("numbers2.txt","r")
# nums2=nums.read()
# print(nums2)


def Barbie(file_name):
    f= open(file_name,"r")
    lines=f.readlines()
    barbie_prices={}
    for i in range(1,len(lines)):
        line=lines[i]
        name,price = line.split("    ")   # => [ "name" , "price" ]
        price=price.strip("\n")
        barbie_prices[name]=price
    return barbie_prices

# x=Barbie("Barbie.txt")
# print(x)

def word_counter(file_name, word):
    counter=0
    f= open(file_name,"r")
    lines=f.readlines()
    for line in lines:
        line_list= line.split(" ")
        for w in line_list:
            w=w.strip("\n")
            if w==word:
                counter+=1
    return counter

# my_word_list=["Ohad", "Animal", "Goat", "Play", "Music"]
# f=open("word.txt", "w")
# for i in range(200):
#     x=random.randint(0,len(my_word_list)-1)
#     f.write(my_word_list[x])
#     f.write("\n")

ohad_counter= word_counter("word.txt","Ohad")
print(ohad_counter)










