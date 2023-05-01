def unique_day(date, possible_birthdays):
    total= 0
    for i in possible_birthdays:
        if date == i[1]:
            total= total + 1
    return total == 1

def unique_month(month, possible_birthdays):
    total= 0
    for i in possible_birthdays:
        if month == i[0]:
            total= total + 1
    return total == 1

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if unique_day(i[1], possible_birthdays):
            return True
    return False
