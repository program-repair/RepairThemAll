def unique_day(day, possible_birthdays):
    counted = ()
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            if day not in counted:
                counted += (day,)
            else:
                return False
    
    return True
    
def unique_month(month, possible_birthdays):
    day = month
    counted = ()
    for birthdays in possible_birthdays:
        if birthdays[0] == day:
            if day not in counted:
                counted += (day,)
            else:
                return False
    
    return True
    
def contains_unique_day(month, possible_birthdays):
    for possiblemonth in possible_birthdays:
        if possiblemonth[0] == month:
            if unique_day(possiblemonth[1],possible_birthdays) == True:
                return True
            else:
                continue
    return False
