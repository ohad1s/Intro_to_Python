my_dict={}
my_dict["ohad"]=7

def char_counter(my_str):
    my_dict = {}
    for char in my_str:
        if char in my_dict.keys():
            my_dict[char]+=1
        else:
            my_dict[char]=1
    max=0
    max_char=""
    # print(my_dict)
    for key ,value in my_dict.items():
        # print(key,value)
        if value>max:
            max=value
            max_char=key
    return max_char


# str1= input("enter a string")
# char= char_counter(str1)
# print(char)
# ========================================
# lst1= [1,2,3,4,56]
# for number in lst1:
#     print(number)
# print(lst1)

students_avgs={"yossi":(78,7),"ohad":(85, 3)}

def enter_grade(grade,name,students_avg):
    if name not in students_avg.keys():
        students_avg[name]=(grade ,1)
    else:
        avg=students_avg[name][0]
        num_grades= students_avg[name][1]
        new_avg=((avg*num_grades)+grade)/(num_grades+1)
        students_avg[name]=(new_avg,num_grades+1)

enter_grade(99, "ohad", students_avgs)
enter_grade(60, "yossi", students_avgs)
enter_grade(99,"daniel",students_avgs)

# print(students_avgs)

# x = int(input("enter a number"))
# y = int(input("enter a number"))
# try:
#     print(x/y)
# except ZeroDivisionError:
#     print("y=0")
# except ValueError:
#     print("not int value")
# except (TypeError, ImportError):
#     print("other error!")
# finally:
#     print("hello world!")

def readFromFile(file):
    counter=0
    try:
        f= open(file, "r")
        # other code
    except FileNotFoundError:
        print("try again!")
        counter=-1
    return counter

def char_counter(char,my_str):
    if len(char)>1:
        raise ValueError("String and not Char Value")
    if type(my_str)!= str:
        raise TypeError(f"{my_str } isn't  a string ")
    if char==my_str:
        raise "MY ERROR!"

# char_counter("abc", "sdfsfew")
# char_counter("a", 9)
# char_counter("a","a")


# "hello" -> "olleh"
# "h" -> "h"
def rev_rec(my_str):
    if len(my_str)==1:
        return my_str
    return rev_rec(my_str[1:])+rev_rec(my_str[0])

print(rev_rec("hello world"))


