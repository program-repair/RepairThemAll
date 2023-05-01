def unique_day(date, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[1] == date:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0] == month:
            if unique_day(birthday[1], possible_birthdays):
                return True
    return False
