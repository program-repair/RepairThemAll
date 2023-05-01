def unique_day(day, possible_birthdays):
    def map(fn,seq):
        if seq == ():
            return ()
        else:
            return (fn(seq[0]),) + map(fn,seq[1:])
    days = map(lambda x: x[1], possible_birthdays)
    filter1 = filter(lambda x:x == day, days)
    tup = tuple(filter1)
    return len(tup) == 1

def unique_month(month, possible_birthdays):
    def map(fn,seq):
        if seq == ():
            return ()
        else:
            return (fn(seq[0]),) + map(fn,seq[1:])
    months = map(lambda x: x[0], possible_birthdays)
    filter2 = filter(lambda x:x == month, months)
    tup2 = tuple(filter2)
    return len(tup2) == 1

def contains_unique_day(month, possible_birthdays):
    days = ()
    for a in possible_birthdays:        
        if a[0] == month:
            days = days + (a[1],)
    for b in days:
        if unique_day(b, possible_birthdays):
            return True
    return False
