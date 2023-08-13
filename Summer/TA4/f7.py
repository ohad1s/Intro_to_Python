def f1(mystr,myint):
    print(mystr*myint)

# x=f1("a",10)
# print(x)


def f2():
    print("Hello World")

# f2()
# print(f2())

def f3():
    return "Ciiiii"
# f3()
# x=f3()
# print(x+" CR7")


def f4(a,b,c):
    return (a+b+c)

# avg=f4(1,2,3)/3
# print(avg)

def moveCharToLast(string,char):
    new_str=""
    counter=0
    for c in string:
        if c==char:
            counter+=1
        else:
            new_str+=c
    return new_str+(counter*char)

# moveCharToLast("hello","l")


def reduce(string):
    new_str=string[0]
    for char in string:
        if char!=new_str[-1]:
            new_str+=char
    return new_str

# print(reduce("aaaaaabccccdddeeerttaa"))





def q1_aviv_b23(string , n)->str:
    my_str=string
    for i in range(n):
        my_str=my_str[-1]+my_str[:-1]
    return my_str[::2]

# print(q1_aviv_b23("abcdefg",2))

# -----------------------------
# f=open("bdika.txt","a")
# f.write("\n")
# f.write("hello")
# f.close()

with open("bdika.txt","r") as f:
    # r= f.read()
    # print(r)
    # r2= f.readline()
    # print(r2)
    # r3= f.readline()
    # print(r3)
    lines=f.readlines()
    # print(lines)
    file_dict={}
    for i, line in enumerate(lines):
        # file_dict[i]=line
        file_dict[i+1]=line.strip("\n").strip("\t")
    print(file_dict)

def q2(file_name,lst1,lst2):
    if len(lst1)!=len(lst2):
        print("Error!")
    else:
        with open(file_name+".txt","w") as f:
            for i in range(len(lst1)):
                f.write(f"{lst1[i]} {lst2[i]}\n")


l1=["a","b","c","d"]
l2=["w","x","y","z"]
q2("check",l1,l2)
number=ord("a")
print(f"the number of a is: {number}")
char=chr(number+18)
print(f"{char}")
def cycle_char(char,num):
    return chr(((ord(char)-ord("a")+num)%26)+ord("a"))


print(cycle_char("z",1))



