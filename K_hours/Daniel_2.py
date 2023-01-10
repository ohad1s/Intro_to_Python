class Home():
    def __init__(self,rooms):
        self.rooms=rooms
        # self.rooms={} # wrong!

    def add_room(self, name, size):
        self.rooms[name]=size

    def resize_room(self,name, to_add):
        self.rooms[name]+=to_add

# my_rooms={"bathroom":20, "toilet":15, "bedroom":30,"kitchen":20}
# home_1= Home(my_rooms)
# your_rooms={}
# home_2= Home(your_rooms)
#
# my_file=open("myfilename.txt","w")
# my_file.write("ohad")
# my_file.write("\n")
# my_file.close()



def luck_num(filename):
    my_file=open(filename,"r")
    if type(filename)!= str:
        raise TypeError("Not a string!")
    lines = my_file.readlines()
    if len(lines)>30:
        raise "Too Much Lines!"
    luck_nums={}
    sum=0
    for line in lines:
        line = line.strip("\n")
        name, num = line.split("-")
        luck_nums[name]=num
        try:
            sum+=num
        except Exception:
            print("Error!- avg will be wrong")
    avg= sum/len(luck_nums)
    return luck_nums, avg


def luck_num_2(filename):
    my_file=open(filename,"r")
    lines = my_file.readlines()
    luck_nums={}
    sum=0
    for line in lines:
        line = line.strip("\n")
        name, num = line.split("-")
        luck_nums[name]=num
        sum+=int(num)
    avg= sum/len(luck_nums)
    return luck_nums, avg

nums_dict, my_avg = luck_num_2("myfilename.txt")
print(my_avg)
print(nums_dict)








