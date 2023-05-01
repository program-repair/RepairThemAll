def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[1] == day:
            count += 1
    if count > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            count += 1
    if count > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    unique_day_tuple = tuple(filter(lambda x: unique_day(x[1],possible_birthdays),possible_birthdays))
    for i in unique_day_tuple:
        if i[0] == month:
            return True
    return False
