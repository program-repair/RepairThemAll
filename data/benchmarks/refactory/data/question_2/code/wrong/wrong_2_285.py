def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == day:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == day:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if i[0] == month:
            tup += ((i),)
        else:
            continue
    for i in tup:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False
