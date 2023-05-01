def unique_day(day, possible_birthdays):
    counter = 0
    for bday in possible_birthdays:
        if day == bday[1]:
            counter += 1   
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for bday in possible_birthdays:
        if month == bday[0]:
            counter += 1   
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for bday in possible_birthdays:
        if month == bday[0]:
            days_in_month += (bday[1],)
    for day in days_in_month:
        if unique_day(day, possible_birthdays) == True:
            return True
    return False
