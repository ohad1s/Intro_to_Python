def is_char_in_str(string1,char):
    if len(string1)==1:
        return string1==char
    return is_char_in_str(string1[0],char) or is_char_in_str(string1[1:],char)


# print(is_char_in_str("abcde","e"))

def is_upper_n(n):
    if type(n)!= int:
        raise TypeError("only integers!")
    if n<0:
        raise ValueError("cant read negative values")
    if n<10:
        return True
    x=n%10
    y=(n%100)//10
    return y>x and is_upper_n(n//10)



