class Student():
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        self.grades={}

    # def __str__(self):
    #     return f"Student: name:{self.name}"

    def __repr__(self):
        return f"Student: name:{self.name}, id: {self.id} grades: {self.grades}"

    def add_grade(self,course, grade):
        self.grades[course]=grade

    def avg_grade(self):
        sum=0
        for grade in self.grades.values():
            sum+= grade
        return sum/len(self.grades)




s1= Student("Ohad","123456789",25)
print(s1)
s2 = Student("Yossi", "123456788", 23)
student_list= [s1,s2]
print(student_list)
s2.add_grade("Python",90)
s2.add_grade("Infi", 60)
s2.add_grade("harta", 88)
print(s2)
print(s2.avg_grade())
print(s2.name)
print(s1.id)




