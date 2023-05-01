def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        counter += 1 if day == birthday[1] else 0
    return (counter == 1)

def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        counter += 1 if month == birthday[0] else 0
    return (counter == 1)

def contains_unique_day(month, possible_birthdays):
    birthdays_in_month = ()
    for birthday in possible_birthdays:
        if birthday[0] == month: birthdays_in_month += (birthday,)
        
    for birthday in birthdays_in_month:
        if unique_day(birthday[1], possible_birthdays):
            return True
    return False
