def unique_day(day, possible_birthdays):
    day_count = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            day_count = day_count + 1
        if day_count > 1:
            break
    if day_count == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    month_count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            month_count = month_count + 1
        if month_count > 1:
            break
    if month_count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    has_unique_day = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            if unique_day(birthday[1], possible_birthdays):
                has_unique_day = 1
                break
    if has_unique_day:
        return True
    else:
        return False
