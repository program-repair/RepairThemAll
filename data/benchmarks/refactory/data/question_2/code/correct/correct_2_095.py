def unique_day(day, possible_birthdays):
    count = 0
    for possible_dates in possible_birthdays:
        if possible_dates[1] == day:
            count += 1
    if count != 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for possible_dates in possible_birthdays:
        if possible_dates[0] == month:
            count += 1
    if count != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    possible_days_in_month = ()
    possible_days_in_others = ()
    for possible_dates in possible_birthdays:
        if possible_dates[0] == month:
            possible_days_in_month += (possible_dates[1],)
        else:
            possible_days_in_others += (possible_dates[1],)
    for day_in_month in possible_days_in_month:
        unique = True
        for day_in_others in possible_days_in_others:
            if day_in_month == day_in_others:
                unique = False
                break
        if unique == True:
            return True
    return False 
