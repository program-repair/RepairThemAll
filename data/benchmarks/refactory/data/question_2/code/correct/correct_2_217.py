def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == date:
            counter += 1
    if counter == 1:
        return True
    return False
    
def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[0] == month:
            counter += 1
    if counter == 1:
        return True
    return False
    
def contains_unique_day(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0] and unique_day(i[1], possible_birthdays):
            return True
    return False
