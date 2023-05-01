def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            counter = counter + 1
    if counter <= 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if birthday[0]== month:
            counter = counter + 1
    if counter <= 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    a =()
    for birthday in possible_birthdays:
        if birthday[0] == month:
            a = a + (birthday,)
    for birthday in a:
        if unique_day(birthday[1], possible_birthdays):
            return True
    return False
