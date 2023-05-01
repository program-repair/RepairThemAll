def unique_day(date, possible_birthdays):
    count = 0
    for possible_birthday in possible_birthdays:
        if day == possible_birthday[1]:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count  = 0
    for possible_birthday in possible_birthdays:
        if month == possible_birthday[0]:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    for possible_birthday in possible_birthdays:
        if month == possible_birthday[0] and unique_day(possible_birthday[1], possible_birthdays):
            return True
    return False
