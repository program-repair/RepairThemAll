def unique_day(day, possible_birthdays):
    counter = 0
    for ele in possible_birthdays:
        birthday = ele[1]
        if birthday == day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False




def unique_month(month, possible_birthdays):
    counter = 0
    for ele in possible_birthdays:
        birthmonth = ele[0]
        if birthmonth == month:
            counter += 1
    if counter == 1:
        return True
    else:
        return False




def contains_unique_day(month, possible_birthdays):
    for ele in possible_birthdays:
        birthmonth = ele[0]
        if birthmonth == month:
            if unique_day(ele[1], possible_birthdays) == True:
                return True
    return False

