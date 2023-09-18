from datetime import datetime
class Person:

    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def __repr__(self):
        return f"Hello i'm {self.name} and i'm {self.age} years old, id: {self.id}"

    def print_hello(self,name):
        print(f"Hello {name}")

    def print_bye(self,name):
        print(f"bye {name}")

class Student(Person):

    def __init__(self,name,age,id,University):
        # bd= datetime.strptime(birthday, '%d/%m/%y')
        # a=((datetime.now().year)-bd.year)
        super().__init__(name,age,id)
        self.__University=University

    def __repr__(self):
        return super().__repr__()+f" and im study in {self.__University}"

    def print_bye(self):
        print(f"bye bro")

    def getUniv(self):
        return self.__University



p1=Person("shir",24,123456787)
s1=Student("ohad",26,123456789,"Ariel")
print(s1)
print(p1)
s1.print_hello("yossi")
s1.print_bye()
# s1.__
u=s1.getUniv()
print(u)