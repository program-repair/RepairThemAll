def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        birthday_day = birthday[1]
        if day == birthday_day:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        birthday_month = birthday[0]
        if month == birthday_month:
            counter += 1
    if counter == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    birthday_days_in_month = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            birthday_days_in_month += (birthday[1],)
    day_counter = 0
    for day in birthday_days_in_month:
        if unique_day(day, possible_birthdays):
            return True
    return False 
