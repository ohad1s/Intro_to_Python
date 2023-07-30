lst=[1,2,3]
tup = (1,2,3,True,"str")
my_elem= tup[0]
tup2= tup
tup.index(True)
# ---------------------
lst2=["ohad",25,"Ariel"]
dicti={"name":"ohad","age":25,"city":"Ariel",1:True}
# dicti2={"lst":[1,3,4],"dicti":{dicti}}

dicti[1]=False
dicti[0]=True
# val= dicti[3]
# print(dicti[0])
# print(val)

dicti3=dicti
print(dicti)
print(dicti3)
dicti["newVal"]="val"
print(dicti)
print(dicti3)
dicti4=dicti.copy()
v1=dicti.pop("name")
dicti.pop("age")
print(v1)
print(dicti)
dicti["check"]=1
x=dicti.popitem()
print(x)
print(dicti)
tups=dicti.items()
print(tups)
keys=dicti.keys()
print(keys)
values=dicti.values()
print(values)
# x1=dicti["name"]
x2=dicti.get("a",0)
print(x2)
# -------------------------------
