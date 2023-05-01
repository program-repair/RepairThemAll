def unique_day(day, possible_birthdays):
    counter = 0
    for date in possible_birthdays:
        if day in date:
            counter += 1
    if counter != 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for date in possible_birthdays:
        if month in date:
            counter += 1
    return True if counter ==1 else False

def contains_unique_day(month, possible_birthdays):
    contains = ()
    for date in possible_birthdays:
        if month in date and unique_day(date[1],possible_birthdays):
            return True
    return False
