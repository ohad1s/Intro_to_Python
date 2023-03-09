class Vehicle():

    def __init__(self, wheels,color,weight):
        self.wheels=wheels
        self.color=color
        self.weight=weight

    def __repr__(self):
        return f"my v: wheels:{self.wheels}, color: {self.color}"

    def drive(self):
        print("im driving..")

    def parking(self):
        print("im parking!!!!")

    def reverse(self):
        print("looking back")


class PublicTransport(Vehicle):

    def __init__(self,wheels,color,weight,seat,price):
        super().__init__(wheels,color,weight)
        self.seat=seat
        self.__price=price

    def __repr__(self):
        return super().__repr__()+f" type of transport: seats: {self.seat}"

    def parking(self):
        print("am i in a parking station?")
        print("parking...")

    def reverse(self):
        super().reverse()
        print(" bip bip")

    def get_price(self):
        return self.__price

    def buy_ticket(self,age):
        if age<=18:
            return self.__price * 0.9
        if age>59:
            return 0
        return self.__price



v1= Vehicle(4,"black",5)
pt= PublicTransport(6,"Grern",12,16,20)

v1.drive()
pt.drive()

v1.parking()
pt.parking()

v1.reverse()
pt.reverse()

my_t= pt.buy_ticket(7)

class Bus(PublicTransport):

    def __init__(self,color,price,driver_name):
        super().__init__(8,color,12,50,price)
        self.cash=0
        self.driver_name=driver_name


bus= Bus("Black", 12,"Ohad")
print(bus)
print(pt)
