# def myName(a,b):
#     c=a+b
#     return c
# #
# # # --------------------- lambda : -------------------------
# z = lambda a: a + 10
# print(z(5))
# y = lambda x: x + x
# # # # why it's good ?
# world_cup= [{"name":"Messi", "goals":10, "assists":7},
#             {"name":"Ronaldo", "goals":8, "assists":2},
#             {"name":"Neymar", "goals":10, "assists":1},
#             {"name":"Mbape", "goals":5, "assists":5},
#             {"name":"Kane", "goals":6, "assists":4}]
# # world_cup.sort()
# # #
# def sort_only_by_goals(player):
#     return player["goals"]
#
# world_cup_sorted=sorted(world_cup,key=sort_only_by_goals)
# world_cup_sorted_2= sorted(world_cup,key=lambda player: (player["goals"],player["assists"]))
# print(world_cup_sorted_2)
# # print("--------")
# my_class=[("ohad", 25,85),("tal", 23,90),("yuval",25,97),("bnaya",26,60),("tair",22,98)]
# my_class_sorted=sorted(my_class,key=lambda student:student[2])
# print(my_class_sorted)

def common_grade(grades_list):
    grades_dict={}
    for g in grades_list:
        if g not in grades_dict.keys():
            grades_dict[g]=1
        else:
            grades_dict[g]+=1
    max_app=0
    max_grade=[]
    for grade, counter in grades_dict.items():
        if counter>max_app:
            max_grade.clear()
            max_app=counter
            max_grade.append(grade)
        elif counter==max_app:
            max_grade.append(grade)
    return max_grade

# print(common_grade([17,11,99,85,85,85,100,100,100]))

def valid_password(password):
    char_flag=False
    upper_flag=False
    lower_flag=False
    digit_flag=False
    special_char="!@#$%^&*()"
    if len(password)<8:
        return False
    for ch in password:
        if ch==" ":
            return False
        if ch.isupper():
            upper_flag=True
        if ch.islower():
            lower_flag=True
        if ch.isdigit():
            digit_flag=True
        if ch in special_char:
            char_flag=True
    return char_flag and upper_flag and lower_flag and digit_flag

# print(valid_password("gertrqetrqe"))

def isPrime(num):
    for i in range(2,num):
        if num%i==0:
            return False
    return True

def isSphenic(number):
    for i in range(2,number):
        if isPrime(i):
            for j in range(2,number):
                if isPrime(j):
                    for k in range(2,number):
                        if isPrime(k):
                            if k*j*i==number and i!=j and i!=k and k!=j:
                                return True
    return False

print(isSphenic(70))

s="Hello World"
k=3
mydict={}
for i in range(0,len(s)-k+1):
    substring=s[i:i+k]
    mydict[substring]=[i,i+k]
print(mydict)


















