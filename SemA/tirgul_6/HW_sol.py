import math
 #https://realpython.com/python-kwargs-and-args/
def moveCharToLast(string,char):
    counter=0
    for c in string:
        if c==char:
            counter+=1
            string=string.replace(c,'')
    string=string+char*counter
    return string

def reduce(string):
    str1 = ""
    str1 += string[0];
    for i in range(1,len(string)):
        if (string[i] != string[i-1]):
            str1 += string[i]
    return str1

def isPrime(number):
    for x in range(2,number):
        if number%x==0:
            return False
    return True

def isMarsennePrime(n):
    if isPrime(n)==False:
        return False
    else:
        for i in range(n):  #  2 ^ i - 1 == n ??
          if (2**i == n+1):
             return True
        return False

def SquareSumNumber(n):
    sum=0
    for i in range(1,n+1):
        if n%i==0:
            sum+=math.pow(i,2)
    if math.pow(int((math.sqrt(sum))),2)==sum:
        return True
    else: return False

def longestCommonSequence(string1,string2):
    str=""
    sum=0
    strToCheck=""
    for i in range(len(string1) + 1):
        for j in range(i,len(string1)+1):
            strToCheck=string1[i:j+1]
            if strToCheck in string2:
                if len(strToCheck)>sum:
                    sum=len(strToCheck)
                    str=strToCheck
    return str

def sphenic(n):
    z=0
    x=0
    y=0
    for i in range(2, n+1):
        if (isPrime(i) and (n/i)%1==0):
            x=i
            p1=int (n/x)
            for j in range(2,p1+1):
                if (isPrime(j) and float(p1 / j) % 1 == 0):
                    y=j
                    p2=int(p1/y)
                    for k in range(2,p2+1):
                        if (isPrime(k) and float(p2 / k) % 1 == 0):
                            z=k
                            if (x!=0 and y!=0 and z!=0):
                                if (x!=z and x!=y and y!=z):
                                    return True
    return False

def maxLenList(l1,l2):
    if len(l1)>len(l2):
        return l1
    else: return l2

def crissCross(l1,l2):
    maxi=maxLenList(l1,l2)
    l3=[]
    for i in range(0,min(len(l1),len(l2))):
        l3.append(l1[i])
        l3.append(l2[i])
    for j in range(min(len(l1),len(l2))+1,max(len(l1),len(l2))):
        l3.append(maxi[j])
    return l3



