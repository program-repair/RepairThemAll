def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            count += 1
    if count == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            count += 1
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    result = ()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            result += (unique_day(birthday[1], possible_birthdays),)
    if any(result):
        return True
    return False
