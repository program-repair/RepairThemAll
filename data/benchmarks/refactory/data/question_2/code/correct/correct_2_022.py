def unique_day(day, possible_birthdays):
    count_day = 0
    for i in possible_birthdays:
        if i[1] == day:
            count_day += 1
    if count_day == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count_month = 0
    for i in possible_birthdays:
        if i[0] == month:
            count_month += 1
    if count_month == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    possible_days = ()
    for i in possible_birthdays:
        if i[0] == month:
            possible_days += (i[1],)
    for i in possible_days:
        if unique_day(i, possible_birthdays) == True:
            return True
    return False
