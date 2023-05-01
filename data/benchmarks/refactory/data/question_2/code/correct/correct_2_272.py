def unique_day(day, possible_birthdays):
    counter = 0
    for item in possible_birthdays:
        if item[1] == day:
            counter = counter + 1
    if counter !=1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for item in possible_birthdays:
        if item[0] == month:
            counter = counter + 1
    if counter != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    dates_in_month = ()
    new_possible_birthdays = ()
    for item in possible_birthdays:
        if month in item:
            dates_in_month += (item[1],)
        elif month not in item:
            new_possible_birthdays += (item[1],)
    result = 0
    for item in dates_in_month:
        if item in new_possible_birthdays:
            result += 1
    if result != len(dates_in_month):
        return True
    else:
        return False 
