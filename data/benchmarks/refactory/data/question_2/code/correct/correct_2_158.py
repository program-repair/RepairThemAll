def unique_day(day, possible_birthdays):
    days = ()
    for elem in possible_birthdays:
        days += (elem[1],)
    times = days.count(day)
    if times == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    months = ()
    for elem in possible_birthdays:
        months += (elem[0],)
    times = months.count(month)
    if times == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    bdays_in_month = ()
    for elem in possible_birthdays:
        if elem[0] == month:
            bdays_in_month += (elem[1],)
        else:
            bdays_in_month = bdays_in_month
    for el in bdays_in_month:
        if unique_day(el, possible_birthdays) == True:
            return True
    return False
