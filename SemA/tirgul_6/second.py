# import csv
# # import math
# # print(math.sqrt(9))
# open_file = open('./results.csv',encoding="utf-8")
# # open_file = open(r'C:\Users\shira\PycharmProjects\SemsterA_22-23\tirgul_6\csv_reading.py')
# games= csv.reader(open_file)
# games_list=list(games)
# header= games_list[0]
# print(header)
# # for row in games_list:
# #     print(row)
# counter_games=0
# counter_goals=0
# tr= "FIFA World Cup"
# for row in games_list:
#     if row[5]==tr:
#         if row[1]=="Israel":
#             print(row)
#             counter_games+=1
#             counter_goals+=int(row[3])
#         if row[2]=="Israel":
#             print(row)
#             counter_games+=1
#             counter_goals+=int(row[4])
# print("Israel Goals: {}, Israel Games: {}, Israel avg per game: {}".format(counter_goals,counter_games,counter_goals/counter_games))
print("------------------------------------------")

def MyName(x,y):
    z=x+y
    return z,x,y

def MyName_2(x,y):
    print("(x:{},y:{})".format(x,y))

# sum=MyName(5,10)
# print(sum)
# MyName_2(10,5)
# a,b,c= MyName(10,20)
# print(a,b,c)

def moveCharToLast(mystr,mychar):
    str_to_return=""
    char_counter=0
    for char in mystr:
        if char==mychar:
            char_counter+=1
        else:
            str_to_return+=char
    str_to_return+=mychar*char_counter
    return str_to_return

mynewchar= moveCharToLast("abababcbdnafbbtbtewkfb","b")
print(mynewchar)

def reduce(mystr):
    str_to_return=""
    for i in range(len(mystr)-1):
        if mystr[i]==mystr[i+1]:
            continue
        else:
            str_to_return+=mystr[i]
    str_to_return+=mystr[-1]
    return str_to_return

print(reduce("ddaffffafaffff"))










