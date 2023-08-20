lst= [7,2,8,3,6,1,9,0,2]
sorted_lst= [1,2,3,4,6,8,9,11,12,15]

def binary_search(lst,i):
    mid=len(lst)//2
    if lst[mid]==i:
        return True
    if len(lst)==1:
        return False
    elif lst[mid]>i:
        new_lst=lst[0:mid]
        return binary_search(new_lst,i)
    else:
        new_lst=lst[mid+1:]
        return binary_search(new_lst, i)


def binary_insert(lst,i):
    start=0
    end=len(lst)-1
    while start<end:
        mid=(start+end)//2
        if lst[mid]<=i<=lst[mid+1]:
            return mid+1
        elif i<lst[mid]:
            end=mid
        else:
            start=mid
    if lst[start]>i:
        return start
    else:
        return end+1





