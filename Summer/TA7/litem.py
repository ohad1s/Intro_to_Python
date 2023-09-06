class item:

    def __init__(self,data):
        self.__data=data
        self.__next=None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_next(self,new_next):
        self.__next=new_next

    def set_data(self,data):
        self.__data=data


def build_lst(listData)->item :
    start=item(listData[0])
    curr=start
    for da in listData[1:]:
        new_item=item(da)
        curr.set_next(new_item)
        curr=curr.get_next()
    return start


    # ["a","b","c"]

