def unique_day(day, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if element[1] == day:
            count += 1
    if count != 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for element in possible_birthdays:
        if element[0] == month:
            count += 1
    if count != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    month_collection = ()
    outside_month_collection = ()
    for element in possible_birthdays:
        if element[0] == month:
            month_collection += (element, )
        else:
            outside_month_collection += (element, )
    for days in month_collection:
        count = 0
        for dates in outside_month_collection:
            if days[1] == dates[1]:
                count += 1
        if count == 0:
            return True
    return False
