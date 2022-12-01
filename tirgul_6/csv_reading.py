import csv
# import math
# print(math.sqrt(9))
open_file = open('./results.csv',encoding="utf-8")
# open_file = open(r'C:\Users\shira\PycharmProjects\SemsterA_22-23\tirgul_6\csv_reading.py')
# games_dict= csv.DictReader(open_file)
games= csv.reader(open_file)
# print(games)
# for row in games:
#     print(row)
#     break

print("------------------")
games_data= list(games)
# print(games_data)
header= games_data[0]
print(header)
Isr_games_counter=0
Isr_goals_counter=0
for row in games_data:
    if row[1]== 'Israel' or row[2]== "Israel":
        print(row)
        Isr_games_counter+=1
    if row[1]=='Israel':
        Isr_goals_counter+=(int(row[3]))
    if row[2]=="Israel":
        Isr_goals_counter+=(int(row[4]))
print("Israel Goals: ", Isr_goals_counter)
print("Israel Games: ", Isr_games_counter)
print("Israel avg goal per game: ", Isr_goals_counter/Isr_games_counter)



