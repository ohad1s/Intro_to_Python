import random

# with open("bdika.txt","r") as f:
#     txt=f.readlines()
#     for line in txt:
#         print(line)
#
# f2= open("bdika2.txt","a")
# f2.write("ohad")
# f2.close()

def enter_number_to_file(file_name):
    with open(file_name,"w") as f:
        for i in range(100):
            x=random.randint(1,100)
            f.write(str(x)+"\n")

# enter_number_to_file("numbers.txt")
def avg_nums(file_name):
    summ=0
    with open(file_name, "r") as f:
        lines=f.readlines()
        for i in lines:
            summ+=int(i)
        return summ/len(lines)

# print(avg_nums("numbers.txt"))

# x=int(input("enter a number"))
# y=int(input("enter a number"))
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("you cant divide be zero")
#     y=1
# except Exception:
#     print("another ERR")
#     y=1
# finally:
#     print(x/y)
#     print("Thanks")

def omer(num):
    if type(num)!=int:
        raise TypeError("number must be integer")
    if num<1 or num > 49:
        raise ValueError("not in range")
    if num==33:
        print("happy lag Baomer")
    print(f"weeks: {num//7}, days: {num%7}")

# omer(33)

def name(full_name):
    if type(full_name)!=str:
        raise TypeError("only str !")
    name=full_name.split(" ")
    if len(name)!=2:
        raise ValueError("bad name!")
    return name[0].upper()+" "+name[1].lower()

print(name("Ohad Shirazi"))