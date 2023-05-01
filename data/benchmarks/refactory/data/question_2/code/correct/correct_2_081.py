def unique_day(day, possible_birthdays):
    count = 0
    for k in possible_birthdays:
        if k[1] == day:
            count = count + 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count = 0
    for k in possible_birthdays:
        if k[0] == month:
            count = count + 1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for k in possible_birthdays:
        if month == k[0] and unique_day(k[1], possible_birthdays)==True:
            return True
    return False

