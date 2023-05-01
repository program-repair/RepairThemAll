def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if day in i:
            count += 1
    if count > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if month in i:
            count += 1
    if count > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        if month in i:
            days += (i[1],)
    for j in days:
        if unique_day(j, possible_birthdays):
            return True
    return False
