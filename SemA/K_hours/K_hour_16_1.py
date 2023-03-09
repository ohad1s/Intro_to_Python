def onOff(lst):
    mylist=[]
    for index, number in enumerate(lst):  # -> tuple (index, content)
        if index%2==0:
            mylist.append(number)
    return mylist

def onOff2(lst):
    mylist=[]
    for i in range(len(lst)):
        if i%2==0:
            mylist.append(lst[i])
    return mylist

def onOff3(lst):
    mylist= lst[0:len(lst):2]
    return mylist

lst= [1,2,3,4,5,6,7,8,9]
lst2=onOff3(lst)
print(lst2)

def get_subst(a,b):
    counter=0
    min_len= min(len(a),len(b))
    for i in range(0,min_len-1):
        if a[i:i+2]==b[i:i+2]:
            counter+=1
    return counter


def gradesList(id,names,grades):
    students_dict={}
    for i in range(len(id)):
        id_i=id[i]
        name_i=names[i]
        grade_i=grades[i]
        value_i={name_i:grade_i}
        students_dict[id_i]=value_i
    return students_dict

def factor(grades_dict, f):
    for id ,inner_dict in grades_dict.items():
        for name, grade in inner_dict.items():
            g=grade+f
            if g>100:
                g=100
            grades_dict[id][name]=g

mylist= [1,2,"sfd",True]
print(mylist)
print("[" ,end=" ")
for element in mylist:
    print(element, end=" ")
print("]")




