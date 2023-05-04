import random

with open("bdika.txt","a") as myfile:
    myfile.write("!")
#q1:
fam_names=["ohad","fother","mother"]
f= open("myfam.txt","w")
for name in fam_names:
    f.write(name+"\n")
#q2:
def stars(num,name):
    with open(name,"w") as f:
        for i in range(1,num+1):
            line="*"*i
            # f.write(i*"*"+"\n")
            f.write(f"{line}\n")
stars(7,"stars.word")

#q5:
with open("numbers.txt","w") as nums:
    for i in range(100):
        x=random.randint(1,100)
        nums.write(str(x))
        nums.write("\n")

def avg_from_file(file_name):
    f= open(file_name,"r")
    nums=f.readlines()
    sum=0
    for i in nums:
        n=int(i)
        sum+=n
    f.close()
    return sum/len(nums)

x=avg_from_file("numbers.txt")
print(x)
# ---------------------------------------
# x=int(input("enter a number"))
# y=int(input("enter a number"))
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("you can divide be zero")
# except Exception:
#     print("another ERR")
# finally:
#     print("Thanks")
# ---------------------------
# def check(number,mystr):
#     if 0<number<10:
#         raise ValueError("bad number")
#     print(mystr*number)
#
# check(5,"o")

def Q1(file_name):
    try:
        with open(file_name,"r")as f:
            lines=f.readlines()
            return lines
    except FileNotFoundError:
        print("The file not exist")
    finally:
        print("Hello World")

Q1("numbers.txt")

def Q3(full_name):
    if type(full_name)!=str:
        raise TypeError("not a string")
    name_lst=full_name.split(" ")
    if len(name_lst)!=2:
        raise ValueError("must be name_lastname")
    return name_lst[0].upper()+" "+name_lst[1].lower()

print(Q3(5))



