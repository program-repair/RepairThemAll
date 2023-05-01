def unique_day(day, possible_birthdays):
    appearance = 0
    for i in possible_birthdays:
        if i[1] == day:
            appearance += 1
    if appearance == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    appearance = 0
    for i in possible_birthdays:
        if i[0] == month:
            appearance += 1
    if appearance == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(i[1],possible_birthdays):
                return True
    return False
