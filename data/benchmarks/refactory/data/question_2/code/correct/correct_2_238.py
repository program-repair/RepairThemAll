def unique_day(day, possible_birthdays):
    """Your solution here"""
    check_day = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(check_day) == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    """Your solution here"""
    check_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(check_month) == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    date_day = ()
    for date in possible_birthdays:
        if date[0] == month:
            date_day += (date[1],)
    for check in date_day: # loop through the tuple date_day, each element gives a day
        check_day = tuple(filter(lambda x: x[1] == check, possible_birthdays))
        if len(check_day) == 1:
            return True
    return False
