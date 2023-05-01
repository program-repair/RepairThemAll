def unique_day(date, possible_birthdays):
    num = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            num += 1
    return num == 1

def unique_month(month, possible_birthdays):
    num = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            num += 1
    return num == 1

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if month == birthday[0]:
            if unique_day(birthday[1], possible_birthdays):
                return True
    return False
