def counter_char(my_str,char):
    counter=0
    for ch in my_str:
        if ch==char:
            counter+=1
    return counter

##### check: ######
x = counter_char("Abcbcbcbc","b")
print(x)
y = counter_char("aaaaaaa","a")
print(y)

print("----------------------")

def fibo(index):
    first=0
    second=1
    for i in range(3,index):
        helper=second
        second=first+second
        first=helper
    return first+second




