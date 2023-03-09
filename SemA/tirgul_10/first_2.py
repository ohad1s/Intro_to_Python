class Student():
    def __init__(self,name,id,age):
        self.name=name
        self.id=id
        self.age=age
        self.grades={}
        self.Dep="IE"

    # def __str__(self):
    #     return f"Student: name: {self.name}, id: {self.id}, age: {self.age}"

    def __repr__(self):
        # return "Student: name: "+ self.name + "id: "+self.id
        return f"Student: name: {self.name}, id: {self.id}, age: {self.age},grades:{self.grades}"

    def addGrade(self, course, grade):
        self.grades[course]=grade

    def avg_grade(self):
        counter=0
        for grade in self.grades.values():
            counter+=grade
        return counter/len(self.grades)








s1=Student("Ohad","123456789",25)
print(s1)
print(type(s1))
print(s1.id)
s2=Student("Michael", "123456788", 24)
print(s2)
print(s2.Dep)
students_class=[s1,s2,5,"ljdfhdsl"]
print(students_class)
s2.addGrade("Python",85)
s2.addGrade("Infi",60)
print(s2)
michael_avg =s2.avg_grade()
print(michael_avg)


