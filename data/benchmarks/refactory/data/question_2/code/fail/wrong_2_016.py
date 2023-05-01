def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def unique_day(day, possible_birthdays):
    days = map(lambda x: x[1], possible_birthdays)
    times = 0
    for i in days:
        if i==day:
            times = times+1
        else:
            continue
    if times>1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    months = map(lambda x: x[0], possible_birthdays)
    times = 0
    for i in months:
        if i==month:
            times = times+1
        else:
            continue
    if times>1:
        return False
    else:
        return True


def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

def contains_unique_day(month, possible_birthdays):
    relevant_dates= filter(lambda x: x[0] == month, possible_birthdays)
    days = map(lambda x: x[1], relevant_dates)
    times = 0
    for i in days:
        if unique_day(i, possible_birthdays):
            times = times+1
        else:
            continue
    if times==0:
        return False
    else:
        return True 
