def unique_day(date, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[1] == date:
            result = result + 1
    if result != 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[0] == month:
            result = result + 1
    if result != 1:
        return False
    else:
        return True
    

def contains_unique_day(month, possible_birthdays):
    tup = ()
    for n in possible_birthdays:
        if n[0] == month:
            tup = tup + ((n), )
        else:
            continue
    for n in tup:
        if unique_day(n[1], possible_birthdays):
            return True
    return False
            

