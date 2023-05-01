def unique_day(day, possible_birthdays):
    x = 0
    for birthday in possible_birthdays:
        if day in birthday:
            x += 1
    if x > 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    x = 0
    for birthday in possible_birthdays:
        if month in birthday:
            x += 1
    if x > 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    results = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            results += (unique_day(birthday[1], possible_birthdays),)
    if True in results:
        return True
    else:
        return False
