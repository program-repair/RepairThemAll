def unique_day(day, possible_birthdays):
    a=''
    for date in possible_birthdays:
        if a== date[1]:
            return False
        elif day ==date[1]:
            a=day
        
    return True


def unique_month(month, possible_birthdays):
    a=''
    for date in possible_birthdays:
        if a== date[0]:
            return False
        elif month ==date[0]:
            a=month
        
    return True

def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if month==date[0]:
            if unique_day(date[1], possible_birthdays):
                return True
    return False
