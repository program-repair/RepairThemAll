def unique_day(day, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[1] == day:
            tup += (i[1],)
    if len(tup) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[0] == month:
            tup += (i[0],)
    if len(tup) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    tup = ()
    for date in possible_birthdays:
        if date[0] == month:
            tup += (date,)
    for bday in tup:
        if unique_day(bday[1], possible_birthdays):
            return True
    return False
