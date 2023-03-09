# def myName(a,b):
#     c=a+b
#     return c
#
# # --------------------- lambda : -------------------------
# z = lambda a: a + 10
# print(z(5))
# y = lambda x: x + x
# # # why it's good ?
# world_cup= [{"name":"Messi", "goals":10, "assists":7},
#             {"name":"Ronaldo", "goals":8, "assists":2},
#             {"name":"Neymar", "goals":10, "assists":1},
#             {"name":"Mbape", "goals":5, "assists":5},
#             {"name":"Kane", "goals":6, "assists":4}]
# #
# # def sort_only_by_goals(player):
# #     return player["goals"]
# #
# #world_cup.sort() #- will not work
# world_cup_sorted= sorted(world_cup,key=lambda player: (player["goals"],player["assists"]),reverse=True)
# print(world_cup_sorted)
# print("--------")
# print(world_cup)
# # world_cup_sorted__= sorted(world_cup,key=)
# mylist= [("ohad", 25, 85), ("moran", 24 , 0), ("shaked", 17, 100), ("oriel", 24,80)]
# mylist_sorted=sorted(mylist,key=lambda student:student[2])
# print(mylist_sorted)
# def sort_stud(s):
#     return s[1],s[2]
# mylist2_sorted=sorted(mylist,key=sort_stud)
# print(mylist2_sorted)
# # world_cup_sorted2= sorted(world_cup, key=lambda player:player["goals"]+player["assists"],reverse=True)
# # world_cup_sorted3=sorted(world_cup,key=sort_only_by_goals,reverse=True)
# # # print(world_cup_sorted)
# # # print(world_cup_sorted2)
# # # print(world_cup_sorted3)

def valid_password(password:str):
    charachters_special="!@#$%^&*()"
    if len(password)<8:
        return False
    Upper=False
    Lower=False
    character=False
    for ch in password:
        if ch==" ":
            return False
        if ch.isupper():
            Upper=True
        if ch.islower():
            Lower=True
        if ch in charachters_special:
            character=True
    return Upper and Lower and character

print(valid_password("a@@@@@Bhf"))

def common_grade(grades_list):
    grades_dict={}
    for g in grades_list:
        if g in grades_dict.keys():
            grades_dict[g]+=1
        else:
            grades_dict[g]=1
    maximum_grade=[]
    maximum_app=0
    for grade , counter in grades_dict.items():
        if counter>maximum_app:
            maximum_grade.clear()
            maximum_app=counter
            maximum_grade.append(grade)
        elif counter==maximum_app:
            maximum_grade.append(grade)
    return maximum_grade

print(common_grade([17,85,85,85,100,100,100,100,92,92,44,44,85]))



