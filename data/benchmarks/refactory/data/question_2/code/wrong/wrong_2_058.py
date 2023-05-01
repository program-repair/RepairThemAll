def unique_day(day, possible_birthdays):
    total_day = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            total_day += 1
    if total_day == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    total_month = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            total_month += 1
    if total_month == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    return 
