class LinkedItem:
    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def set_data(self,data):
        self.__data=data

    def get_next(self):
        return self.__next

    def set_next(self,next):
        self.__next=next



example= ["a","b","c","d","e"]

def build_lst(list_data):
    head=LinkedItem(list_data[0])
    last=head
    for d in list_data[1:]:
        new_item=LinkedItem(d)
        last.set_next(new_item)
        last=last.get_next()
    return head

my_ll=build_lst(example)

def print_lst(lstItem):
    if lstItem==None:
        print("empty list")
    else:
        while lstItem!=None:
            print(lstItem.get_data())
            lstItem=lstItem.get_next()

# print_lst(my_ll)

# l1=LinkedItem("r")
# l2=LinkedItem("r2")
# l3=LinkedItem("r3")
# l4=LinkedItem("r4")
# l5=LinkedItem("r5")
# l6=LinkedItem("r6")
# l1.set_next(l2)
# l2.set_next(l3)
# l3.set_next(l4)
# l4.set_next(l5)
# l5.set_next(l6)
#
# print_lst(l4)