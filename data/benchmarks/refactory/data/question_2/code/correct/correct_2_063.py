def unique_day(day, possible_birthdays):
    unique = ()
    for birthday in possible_birthdays:
        if day == birthday[1]:
            unique = unique + (day,)
    if len(unique) == 1:        
        return True
    return False

def unique_month(month, possible_birthdays):
    unique = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            unique = unique + (month,)
    if len(unique) == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    correct_months = ()
    for birthday in possible_birthdays:
        if unique_day(birthday[1], possible_birthdays):
            correct_months = correct_months + (birthday[0],)
    if month in correct_months:
        return True
    return False 
