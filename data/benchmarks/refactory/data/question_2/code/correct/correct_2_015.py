def unique_day(day, possible_birthdays):
    count = 0
    days = map(lambda x:x[1], possible_birthdays)
    for i in days:
        if i == day:
            count += 1
    if count != 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    months = map(lambda x:x[0], possible_birthdays)
    for i in months:
        if i == month:
            count += 1
    if count != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    months = map(lambda x:x[0], possible_birthdays)
    for birthday in possible_birthdays:
        if birthday[0] == month:
            if unique_day(birthday[1], possible_birthdays):
                return True
    return False
