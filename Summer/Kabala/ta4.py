def are_all_chars_the_same(string):
    for char in string:
        if char!=string[0]:
            return False
    return True


def q2_2(my_str,k):
    for i in range(len(my_str)-k+1):
        curr=my_str[i:i+k]
        if are_all_chars_the_same(curr):
            return curr
    return "None of above"



def f(poly,x):
    sum=0
    for i,num in enumerate(poly):
        sum+=((x**i)*num)
    return sum

poly1= [3,8,9.2,-1]
x= 3
print(f(poly1,x))


def create_menu(dishes, prices)->dict :
    if len(dishes)!=len(prices):
        raise ValueError("Error!")
    else:
        new_dict={}
        for i in range(len(dishes)):
            new_dict[dishes[i]]=prices[i]
    return new_dict

def reverse_phrase(string)-> str :
    lst=string.split(" ")
    lst.reverse()
    str1=""
    for word in lst:
        str1+=word
        str1+=" "
    return str1[:-1]

print(reverse_phrase("I love py"))

def reverse_phrase2(string)-> str :
    lst=string.split(" ")
    lst.reverse()
    return " ".join(lst)

print(reverse_phrase("I love py"))

