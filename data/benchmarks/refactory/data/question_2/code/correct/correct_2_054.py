def filter(pred, seq):
    res = ()
    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

def unique_day(day, possible_birthdays):
    return len(filter(lambda x:x[1]==day, possible_birthdays)) == 1

def unique_month(month, possible_birthdays):
    return len(filter(lambda x:x[0]==month, possible_birthdays)) == 1

def contains_unique_day(month, possible_birthdays):
    bdays_in_mth = filter(lambda x:x[0]==month, possible_birthdays)
    for bday in bdays_in_mth:
        if unique_day(bday[1], possible_birthdays):
            return True
    return False
