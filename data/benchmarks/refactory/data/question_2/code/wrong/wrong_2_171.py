def unique_day(day, possible_birthdays):
    result = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(result) == 1:
        return True  
    else:
        return False

def unique_month(month, possible_birthdays):
    result = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(result) == 1:
        return True  
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    months = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    result = tuple(filter(lambda y: unique_day(y[1], possible_birthdays), months))
    if len(result) == 1:
        return True
    else:
        return False
