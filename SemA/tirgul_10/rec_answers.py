# ------------------ Solution for ex4 from last year (q1- q6) ---------------------
# -------    Q1   ----------------
def value_of_digit(number, digit):
    if number==0 and digit==0:
        return 1
    if number == 0:
        return 0
    if number % 10 == digit:
        return 1
    return 10 * value_of_digit(number // 10, digit)

# print(value_of_digit(585, 5))
# print(value_of_digit(342, 4))
# print(value_of_digit(572, 5))
# print(value_of_digit(1942, 8))
# print(value_of_digit(1902, 0))
# print(value_of_digit(1920, 0))
# print(value_of_digit(0, 1))
# print(value_of_digit(0, 0))

# -------    Q2   ----------------
def is_char_in_str(char,my_str):
    if len(my_str)==1:
        if my_str==char:
            return True
        else:
            return False
    return my_str[0]==char or is_char_in_str(char,my_str[1:])

# print(is_char_in_str("c","abc"))
# print(is_char_in_str("z","abc"))
# print(is_char_in_str("a","abc"))
# print(is_char_in_str("b","abc"))
# print(is_char_in_str("c","abcc"))

# -------    Q3   ----------------
def is_going_up(n):
    if n<10:
        return True
    return ((n%10)<((n//10)%10) and is_going_up(n//10))

# print(is_going_up(75432))
# print(is_going_up(12345))
# print(is_going_up(12383))
# print(is_going_up(7653421))


# -------    Q4   ----------------
def rev_rec(my_str):
    if not isinstance(my_str, str):
        raise TypeError
    if len(my_str)==1:
        return my_str
    return my_str[-1]+rev_rec(my_str[0:-1])

# print(rev_rec("Hello World"))
# print(rev_rec("ABA"))
# print(rev_rec("Champions"))
# print(rev_rec("רק פושטק עלוב בולע קטשופ קר"))


# -------    Q5   ----------------
def count_small_in_big(small, big):
    if len(big)==len(small):
        if big==small:
            return 1
        return 0
    mid=len(small)
    return count_small_in_big(small, big[:mid])+count_small_in_big(small,big[1:])

# print(count_small_in_big("aba","abababbababa"))
# print(count_small_in_big("i"," ciiiiiiiiIIIiii"))
# print(count_small_in_big("lmbeq","lm10isbetterthencr7"))
# print(count_small_in_big("cic","cicicicicicicic"))


# -------    Q6   ----------------
def index_in_1upSeria(n):
    if n==1:
        return 1
    return (n-1)+(index_in_1upSeria(n-1))

# print(index_in_1upSeria(2))
# print(index_in_1upSeria(4))
# print(index_in_1upSeria(7))
# print(index_in_1upSeria(22))