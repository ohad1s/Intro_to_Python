import csv
open_file = open('./results.csv', encoding="utf-8")
# games_dict= csv.DictReader(open_file)
games= csv.reader(open_file)
# for row in games:
#     print(row)
print("------------------")
games_data= list(games)
print(games_data[0])
header= games_data[0]
Icounter=0
Igoals=0
for game in games_data:
    if game[1]=='Israel' or game[2]=="Israel":
        print(game)
        Icounter+=1
    if game[1]=='Israel':
        Igoals+=int(game[3])
    if game[2] == 'Israel':
        Igoals += int(game[4])
print("Israel Goals: ", Igoals)
print("Israel Games: ", Icounter)
print("Israel avg goal per game: ", Igoals/Icounter)


