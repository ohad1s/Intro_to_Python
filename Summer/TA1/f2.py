x = int (input("enter a number"))
if x<0:
    print("negative")
    print("hello")
elif x==0:
    print("0")
else:
    print("positive")
    print("hello2")
    print("hello3")

print("finished")
#
#
# # ----------------
age = int(input("enter your age"))
if age<18:
    if age<8:
        print("child")
    elif 8<=age<=12:
        print("young")
    else:
        print("mini adult")
else:
   gender= input("enter your g")
   if gender == "male":
       print("Ciiii")
   elif gender == "female":
       print("booz")
   else:
       print("Error!")


my_str= "bdika"
# my_str[0]="q" --> Error
new_val=my_str.replace("k","t")
print(new_val)



mylist=[2,7,3, True,"DANI"]
print(mylist[1])
print(mylist)
mylist[0]=177
print(mylist)
mylist.append(8)
mylist.insert(3,12)
print(mylist)
mylist.append([7,9,2])
print(mylist)
mylist.extend([7,9,2])
print(mylist)
my_pop=mylist.pop(2)
print(my_pop)
print(mylist)
dani_ind= mylist.index("DANI")
mylist.remove("DANI")
print(mylist)

new_list= mylist.reverse()
print(mylist)
print(new_list)
# mylist.sort()

stri= "ohdaddd"
new_stri = stri.strip("d")
new_stri2 =stri.replace("d","E")
print(new_stri2)

# in

print(5 in [1, 2])

a=5
b=a
a+=3
print(a)
print(b)

lista=[2,4,6,8,9]
listb=lista
listc= lista.copy()
lista[0]=999
print(lista)
print(listb)
print(listc)


