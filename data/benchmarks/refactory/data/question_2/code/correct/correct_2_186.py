def unique_day(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if date == i[1]:
            count += 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if month == i[0]:
            count += 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    months = ()
    for i in possible_birthdays:
        if i[0] == month:
            months = months + (i,)
        else:
            continue
    for i in months:
        if unique_day(i[1], possible_birthdays) == True:
            return True
        else:
            continue
    return False

