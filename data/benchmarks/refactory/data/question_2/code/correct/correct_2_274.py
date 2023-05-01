def unique_day(day, possible_birthdays):
    counter = 0
    for elem in possible_birthdays:
        birthday = elem[1]
        if birthday == day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for elem in possible_birthdays:
        birthmonth = elem[0]
        if birthmonth == month:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for elem in possible_birthdays:
        birthmonth = elem[0]
        if birthmonth == month:
            if unique_day(elem[1], possible_birthdays) == True:
                return True
    return False
