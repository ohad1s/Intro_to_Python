class Person:

    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def __repr__(self):
        return f"Hello i'm {self.name} and i'm {self.age} years old, id: {self.id}"

    def print_hello(self,name):
        print(f"Hello {name}")

class Student(Person):

    serial_number=0
    skills=["Math","English","Word"]

    def __init__(self,name,age,id,University):
        super().__init__(name,age,id)
        self.University=University
        Student.serial_number+=1
        self.serial_num=Student.serial_number
        self.my_skills=Student.skills.copy()

    def add_skill(self,new_skill):
        self.my_skills.append(new_skill)

#
s1= Student("ohad",26,123456789,"Ariel")
# s2= Student("ohad2",26,223456789,"Ariel")
# s1.id
# s2.id
# print(s1.serial_number)
# print(s2.serial_number)
# print(Student.serial_number)
# Student.serial_number=3
# s3= Student("ohad3",26,323456789,"Ariel")
# print(s3.serial_number)
# print(s1.serial_number)
# s3.serial_number=5
# s_list=[]
# print(Student.serial_number)
# for i in range(10):
#     s=Student("a",14,12,"Ariel")
#     print(s.serial_num)
# print(Student.serial_number)
# print(s1.serial_number)
# Student.serial_number=5
# print(Student.serial_number)
print(s1.my_skills)
s1.add_skill("py")
print(s1.my_skills)
print(Student.skills)


