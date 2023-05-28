def best_letter(word):
    if len(word)==1:
        return word[0]
    letter= word[0]
    rec_letter= best_letter(word[1:])
    if letter<rec_letter:
        return letter
    return rec_letter

# print(best_letter("bfarg"))

def best_letter_in_sen_lst(sen):
    if len(sen)==1:
        return best_letter(sen[0])
    letter= best_letter(sen[0])
    letter_rec= best_letter_in_sen_lst(sen[1:])
    if letter<letter_rec:
        return letter
    return letter_rec


def best_letter_in_sen(sen):
    lst=sen.split(" ")
    return best_letter_in_sen_lst(lst)

