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
        if month == birthday[0]:
            count += 1
        if count > 1:
            return False
    return True

def contains_unique_day(month, possible_birthdays):
    birthdays_month = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            birthdays_month += (birthday,)
    for birthday in birthdays_month:
        if unique_day(birthday[1], birthdays_month):
            return True
    return False  
