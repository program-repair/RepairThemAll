def unique_day(day, possible_birthdays):
    total = 0
    for i in possible_birthdays:
        if i[1] == day:
            total += 1
    if total > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    total = 0
    for i in possible_birthdays:
        if i[0] == month:
            total += 1
    if total > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(i[1],possible_birthdays):
                return True
    return False
