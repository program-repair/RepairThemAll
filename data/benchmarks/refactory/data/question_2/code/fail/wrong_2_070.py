def unique_day(day, possible_birthdays):
    unique = False
    for i in possible_birthdays:
        if day == i[1]:
            if unique:
                return False
            else:
                unique = True
    return True

def unique_month(month, possible_birthdays):
    unique = False
    for i in possible_birthdays:
        if month == i[0]:
            if unique:
                return False
            else:
                unique = True
    return True

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if month == i[0]:
            if unique_day(i[1],possible_birthdays):
                return True
    return False
