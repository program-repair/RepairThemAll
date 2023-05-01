def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            count += 1
        if count > 1:
            return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[1]:
            count += 1
        if count > 1:
            return False
    return True

def contains_unique_day(month, possible_birthdays):
    return 
