def unique_day(day, possible_birthdays):
    x = ()
    for i in range (0,len(possible_birthdays)):
        x += (possible_birthdays[i][-1],)
    if x.count(day) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    y = ()
    for i in range (0,len(possible_birthdays)):
        y += (possible_birthdays[i][0],)
    if y.count(month) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for x in possible_birthdays:
        if month == x[0]:
            if unique_day(x[-1],possible_birthdays):
                return True
    return False
