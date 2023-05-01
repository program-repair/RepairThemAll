def unique_day(day, possible_birthdays):
    if (tuple(map(lambda x: x[1], possible_birthdays))).count(day) == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    if (tuple(map(lambda x: x[0], possible_birthdays))).count(month) == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    b =()
    for p in possible_birthdays:
        if month == p[0]:
            b += (p[1],) #tuple of all the days of that month
    for d in b:
        if unique_day(d, possible_birthdays) == False:
            continue
        return True
    return False

