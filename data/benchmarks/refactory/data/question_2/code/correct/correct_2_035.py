def unique_day(day, possible_birthdays):
    count = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[1] == day:
            count += 1
        continue
    if count == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[0] == month:
            count += 1
        continue
    if count == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for possible_birthday in possible_birthdays:
        if possible_birthday[0] == month:
            days_in_month += (possible_birthday[1],)
        continue
    for day in days_in_month:
        if unique_day(day, possible_birthdays) == True:
            return True
        continue
    return False 
