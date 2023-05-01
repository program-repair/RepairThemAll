def unique_day(date, possible_birthdays):
    unique_day = ()
    days = ()
    for i in possible_birthdays:
        days += (i[1],)
    for i in days:
        if i == date:
            unique_day += (i,)
        else:
            continue
        
    if len(unique_day) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
