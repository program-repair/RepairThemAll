def unique_day(date, possible_birthdays):
    dates = ()
    for d in possible_birthdays:
        dates += (d[1],)
    if dates.count(date) == 1:
        return True
    else:
        return False
        

def unique_month(month, possible_birthdays):
    months = ()
    for a in possible_birthdays:
        months += (a[0],)
    if months.count(month) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    dates = ()
    for z in possible_birthdays:
        if unique_day(z[1], possible_birthdays):
            dates += (z,)
        else:
            continue
    for i in dates:
        if i[0] == month:
            return True
    else:
        return False
