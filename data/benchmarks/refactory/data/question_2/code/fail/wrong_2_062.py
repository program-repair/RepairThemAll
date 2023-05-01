def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

def unique_day(day, possible_birthdays):
    store = ()
    for birthday in possible_birthdays:
        if birthday[1] == day:
            store += (birthday[1],)
    n = len(store)
    if n >1:
        return False
    return True

def unique_month(month, possible_birthdays):
    store= ()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            store += (birthday[0],)
    n = len(store)
    if n >1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    month1 = filter(lambda x: x[0] == month, possible_birthdays)
    for birthday in month1:
        x = unique_day(birthday[1], possible_birthdays)
        if x == True:
            return True
    return False
