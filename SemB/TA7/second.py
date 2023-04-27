import csv  # from csv import reader
open_file = open('results.csv', encoding="utf-8")
games= csv.reader(open_file) # reader
games_data= list(games)
open_file.close()
# print(games_data)
counter=0
for row in games_data:
    if row[1]=="Israel" or row[2]=="Israel":
        counter+=1
print(f"Israel played {counter} games")




open_file = open('results.csv',"r", encoding="utf-8")
data=open_file.readlines()
for row in data:
    line=row.split(",")
open_file.close()



with open('results.csv',"r", encoding="utf-8") as open_file:
    data=open_file.readlines()
    counter={}
    for row in data:
        line=row.split(",")
        if line[5]=="FIFA World Cup":
            home=line[1]
            away=line[2]
            counter[home]=counter.get(home,0)+int(line[3])
            counter[away]=counter.get(away,0)+int(line[4])
print(counter)
print(max(counter,key=counter.get)) # get the key with the max value

# lambda :
x=["bac", "bdr","btr","bbb"]
xx=sorted(x,key=lambda s: s[1])
print(xx)



