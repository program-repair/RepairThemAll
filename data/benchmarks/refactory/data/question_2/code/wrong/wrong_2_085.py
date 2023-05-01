def unique_day(day, possible_birthdays):
    days = ()
    for birthday in possible_birthdays:
        if birthday[1] != day:
            continue
        elif birthday[1] not in days:
            days += (birthday[1],)
        else:
            return False
    return True

def unique_month(month, possible_birthdays):
    days = ()
    for birthday in possible_birthdays:
        if birthday[0] != month:
            continue
        elif birthday[0] not in days:
            days += (birthday[0],)
        else:
            return False
    return True

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0] != month:
            continue
        else:
            if unique_day(birthday[1],possible_birthdays) == True:
                return True
    return False
