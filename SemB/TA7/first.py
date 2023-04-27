import csv  # from csv import reader
open_file = open('results.csv', encoding="utf-8")
games= csv.reader(open_file) # reader
games_data= list(games)
counter_israel_games=0
for i,row in enumerate(games_data):
    if i==0:
        continue
    if row[1]=="Israel" or row[2]=="Israel":
        counter_israel_games+=1
print(f"Israel played {counter_israel_games} games")

with open('results.csv', 'r',encoding="utf-8") as open_file:
    data= open_file.readlines()
    counter=0
    for line in data:
        row= line.split(",")
        if row[1]=="Israel":
            counter+=int(row[3])
        if row[2]=="Israel":
            counter+=int(row[4])
print(counter)
print(counter/counter_israel_games)

with open('results.csv', 'r',encoding="utf-8") as open_file:
    data= open_file.readlines()
    for line in data:
        row= line.split(",")
        if (row[1]=="Israel" or row[2]=="Israel") and row[5]=="FIFA World Cup":
            print(line)


with open('results.csv', 'r',encoding="utf-8") as open_file:
    data= open_file.readlines()
    for line in data:
        row= line.split(",")
        if row[5]=="FIFA World Cup":
            if (row[1] == "Israel" and int(row[3])>0):
                print(row[0])
            if (row[2] == "Israel" and int(row[4]) > 0):
                print(row[0])

