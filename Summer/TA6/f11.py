def sum_up(n):
    sumi=0
    for i in range(n+1):
        sumi+=i
    return sumi

def sum_up_rec(n):
    if n==1:
        return 1
    return n+sum_up_rec(n-1)


def palindrome_rec(my_str):
    if len(my_str)<=1:
        return True
    return my_str[0]==my_str[-1]  and palindrome_rec(my_str[1:-1])

def min_lst_rec(lst):
    if len(lst)==1:
        return lst[0]
    # min(lst[0],min_lst_rec(lst[1:]))
    first=lst[0]
    rest=min_lst_rec(lst[1:])
    if first>rest:
        return rest
    else:
        return first



