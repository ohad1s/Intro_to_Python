def is_small_in_big(small, big):
    if len(big)==len(small):
        if big==small:
            return 1
        return 0
    return is_small_in_big(small,big[0:len(small)])+is_small_in_big(small,big[1:])


def is_upper_seria_n(n):
    if n<10:
        return True
    x= n%10
    y= (n%100)//10
    return y>x and is_upper_seria_n(n//10)