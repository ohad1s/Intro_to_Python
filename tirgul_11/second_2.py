import datetime


class Client():
    def __init__(self,nickname,first,last,email):
        self.nickname=nickname
        self.first_name=first
        self.last_anme=last
        self.email=email
        self.orders=[]

    def makeOrder(self,itemID, itemName, deliveryMethod="regular"):
        order=Order(itemID, itemName, deliveryMethod)
        self.orders.append(order)

    def cancelOrder(self, itemID):
        for order in self.orders:
            if order.IDnum==itemID:
                self.orders.remove(order)
                break



class Order():

    def __init__(self,IDnumber,ItemName,deliveryMethod):
        self.IDnum=IDnumber
        self.ItemName=ItemName
        self.delivetyMethod=deliveryMethod
        self.openingDate=datetime.date.today()
        self.shipment= Shipment()

    def __repr__(self):
        return f"name: {self.ItemName}, ID: {self.IDnum}, date: {self.openingDate}"


class Shipment():
    def __init__(self):
        pass






