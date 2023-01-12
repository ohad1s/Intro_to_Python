def median(lst):
    lst_len=len(lst)
    if lst_len%2==0:
        i1=lst_len/2
        i2=i1-1
        return (lst[i1]+lst[i2])/2
    else:
        index=lst_len//2
        return lst[index]

def product(x,y):
    if y==0:
        return 0
    if y==1:
        return x
    return x+product(x,y-1)