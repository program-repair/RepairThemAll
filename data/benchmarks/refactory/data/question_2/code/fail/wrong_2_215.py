def map(fn, seq):
    res = ()

    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()

    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res

def unique_day(day, possible_birthdays):
    a = map(lambda x : x[1], possible_birthdays)
    for i in  a:
        if i == day:
            b = filter(lambda x: x == i, a)
            if len(b) > 1:
                return False
            else:
                return True

def unique_month(month, possible_birthdays):
    a = map(lambda x : x[0], possible_birthdays)
    for i in  a:
        if i == month:
            b = filter(lambda x: x == i, a)
            if len(b) > 1:
                return False
            else:
                return True

def contains_unique_day(month, possible_birthdays):
    a = map(lambda x : x[0], possible_birthdays)
    b = map(lambda x : x[1], possible_birthdays)
    k = ()
    for i in range(len(a)):
        if month == a[i]:
                k += (b[i],)
    for f in range(len(k)):
        if len(filter(lambda x: x == k[f],b)) == 1:
            return True
    return False
