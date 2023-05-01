def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if month == birthday[0]:
            if unique_day(birthday[1], possible_birthdays):
                return True
    return False
