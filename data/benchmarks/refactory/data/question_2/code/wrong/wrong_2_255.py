def unique_day(day, possible_birthdays):
    """Your solution here"""
    count = 0
    for element in possible_birthdays:
        if day == element[1]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    """Your solution here"""
    count = 0
    for element in possible_birthdays:
        if month == element[0]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    """Your solution here"""
    for date in possible_birthdays:
        if unique_day(date[1], possible_birthdays) and date[0] == month:
            return True
    else:
        return False
