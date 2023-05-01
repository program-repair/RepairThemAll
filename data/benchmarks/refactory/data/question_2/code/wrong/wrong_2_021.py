def unique_day(day, possible_birthdays):
    possible_days = tuple(map(lambda x: x[1], possible_birthdays))
    counter = 0
    for possible_day in possible_days:
        if day == possible_day:
            counter = counter + 1
    if counter == 1:
        return True
    elif counter > 1:
        return False
    else:
        return "Not a day in possible_birthdays"

def unique_month(month, possible_birthdays):
    possible_months = tuple(map(lambda x: x[0], possible_birthdays))
    counter = 0
    for possible_month in possible_months:
        if month == possible_month:
            counter = counter + 1
    if counter == 1:
        return True
    elif counter > 1:
        return False
    else:
        return "Not a month in possible_birthdays"  

def contains_unique_day(month, possible_birthdays):
    def contains_month(month, elem):
        return month == elem[0]
    pos_bd_containing_month = tuple(filter(lambda x: contains_month(month, x), possible_birthdays))
    for element in pos_bd_containing_month:
        if unique_day(element[1], possible_birthdays) == True:
            return True
    return False
