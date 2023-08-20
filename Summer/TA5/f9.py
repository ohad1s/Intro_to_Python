import csv  # from csv import reader
open_file = open('results.csv', encoding="utf-8")
games= csv.reader(open_file) # reader
games_data= list(games)
# print(games_data)
# -------------------------------------------------------------
counter_israel_games=0
header={}
for i,row in enumerate(games_data):
    if i==0:
        for index,elem in enumerate(row):
            header[elem]=index
        print(header)
    if row[header["home_team"]]=="Israel" or row[header["away_team"]]=="Israel":
        counter_israel_games+=1
print(f"Israel played {counter_israel_games} games")
# ------------------------------------------------------------
counter_israel_goals=0
for i,row in enumerate(games_data):
    if i==0:
        for index,elem in enumerate(row):
            header[elem]=index
    if row[header["home_team"]]=="Israel":
        counter_israel_goals+=int(row[header["home_score"]])
    elif row[header["away_team"]]=="Israel":
        counter_israel_goals+=int(row[header["away_score"]])
print(f"Israel played {counter_israel_goals} games")
# ------------------------------------------------------------
counter_goals={}
for i,row in enumerate(games_data):
    if i==0:
        for index,elem in enumerate(row):
            header[elem]=index
    if row[header["tournament"]]=="FIFA World Cup":
        home=row[header["home_team"]]
        away=row[header["away_team"]]
        home_g=int(row[header["home_score"]])
        away_g=int(row[header["away_score"]])
        # print(home,away,home_g,away_g)
        counter_goals[home]=counter_goals.get(home,0)+home_g
        counter_goals[away] = counter_goals.get(away, 0) + away_g
print(counter_goals)
# maxi= max(counter_goals, lambda tup: tup[1])
# print(maxi)
# ----------------------------------------------------------
def create_menu(dishes, prices)->dict :
    if len(dishes)!=len(prices):
        raise ValueError("lists length are not equal")
    dicti={}
    for d, p in zip(dishes,prices):
        # print(d,"----",p)
        dicti[d]=p
    return dicti

dishes = ['Pad-Tai Chicken', 'Fish & Fries' , 'Ice cream waffle']
prices = [75.0, 60.0, 45.0]

dishes_d=create_menu(dishes,prices)
print(dishes_d)

def save_menu_orig(menu,filename):
    if filename[len(filename)-4:]!=".csv":
        raise ValueError("must be a csv file")
    with open(filename,"w")as myfile:
        myfile.write("dish,price,currency\n")
        for dish, price in menu.items():
            myfile.write(f"{dish},{price},NIS\n")

save_menu_orig(dishes_d,"menu2.csv")


def save_menu(menu,filename):
    with open(filename+".csv","w") as myfile:
        myfile.write("dish,price,curr\n")
        for d, p in menu.items():
            myfile.write(f"{d},{p},NIS\n")
d={'Pad-Tai Chicken': 75.0, 'Fish & Fries': 60.0, 'Ice cream waffle': 45.0}
save_menu(d,"my_menu")


