def unique_day(day, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if day == i[1]:
            result = result + 1

    if result == 1:
        return True

    else:
        return False

def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if month == i[0]:
            result = result + 1

    if result == 1:
        return True
    
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    return 
