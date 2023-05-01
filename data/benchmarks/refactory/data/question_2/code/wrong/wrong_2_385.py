def unique_day(date, possible_birthdays):
    counter = 0
    for birthdate in possible_birthdays:
        if str(date) == birthdate[1]:
            counter += 1
    if counter > 1:
        return False
    else:
        return True
            

def unique_month(month, possible_birthdays):
    counter = 0
    for birthdate in possible_birthdays:
        if month == birthdate[0]:
            counter += 1
    if counter > 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    for birthdate in possible_birthdays:
        if month == birthdate[0]:
            return unique_day(birthdate[1], possible_birthdays)
