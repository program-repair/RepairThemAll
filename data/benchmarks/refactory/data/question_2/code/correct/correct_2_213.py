def unique_day(date, possible_birthdays):
    uniqueday = ()
    days = ()
    for i in possible_birthdays:
        days += (i[1],)
    for i in days:
        if i == date:
            uniqueday += (i,)
        else:
            continue
        
    if len(uniqueday) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    uniquemonth = ()
    months = ()
    for i in possible_birthdays:
        months += (i[0],)
    for i in months:
        if i == month:
            uniquemonth += (i,)
        else:
            continue
        
    if len(uniquemonth) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    choose_month = ()
    uniqueday_in_month = ()
    
    for i in possible_birthdays:
        if i[0] == month:
            choose_month += (i,)
        else:
            continue
   
    for i in choose_month:
        if unique_day(i[1], possible_birthdays) == True:
            return True
    return False
