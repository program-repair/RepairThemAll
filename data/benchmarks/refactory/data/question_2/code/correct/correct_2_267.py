def unique_day(date, possible_birthdays):
    if len(tuple(filter(lambda x: x[1] == date, possible_birthdays))) != 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    if len(tuple(filter(lambda x: x[0] == month, possible_birthdays))) != 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    singledays = tuple(filter((lambda x: unique_day(x[1], possible_birthdays)), possible_birthdays))
    for i in singledays:
        if i[0] == month:
            return True
    return False
    
