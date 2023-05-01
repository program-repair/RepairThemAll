def unique_day(day, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if day in i:
            result = result + 1
    if result > 1:
        return False
    elif result == 0:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if month in i:
            result = result + 1
    if result > 1:
        return False
    elif result == 0:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    month_tup = ()
    for i in possible_birthdays:
        if month in i:
            month_tup = month_tup + possible_birthdays[i]
    return unique_day(day, month_tup)
    
