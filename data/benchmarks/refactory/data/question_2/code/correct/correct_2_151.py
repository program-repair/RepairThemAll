def unique_day(day, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        days += (i[1],)
    count = 0
    for ele in days:
        if ele == day:
            count += 1
    if count == 1:
        return True
    else:
        return False
        
def unique_month(month, possible_birthdays):
    months = ()
    for i in possible_birthdays:
        months += (i[0],)
    count = 0
    for ele in months:
        if ele == month:
            count += 1
    if count == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    possible_birthdays_in_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for i in possible_birthdays_in_month:
        if unique_day(i[1], possible_birthdays):
            return True
    else:
        return False
