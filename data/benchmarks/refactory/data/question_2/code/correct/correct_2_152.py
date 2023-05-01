def unique_day(day, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        x += (i[1],)
    for i in x:
        if i == day:
            y += (i,)
        else:
            continue
    if len(y) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        x += (i[0],)
    for i in x:
        if i == month:
            y += (i,)
        else:
            continue
    if len(y) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    x = ()
    y = ()
    for i in possible_birthdays:
        if i[0] == month:
            x += (i,)
        else:
            continue
    for i in x:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False
