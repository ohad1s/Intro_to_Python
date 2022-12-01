def FuncName(x,y):
    z=x+y
    return z

def isPalindrome(mystr):
    str_len_half=len(mystr)//2
    for i in range(0,(str_len_half)):
        j=len(mystr)-i-1
        if mystr[i]!=mystr[j]:
            return False
    return True

myname="ABcBcBA"
myname_isPalindrome=isPalindrome(myname)
print(myname_isPalindrome)
myname2="sdkjfadsf"
print(isPalindrome(myname2))
