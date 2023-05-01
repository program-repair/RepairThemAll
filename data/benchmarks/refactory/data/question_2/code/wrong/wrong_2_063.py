def unique_day(day, possible_birthdays):
    bag = ()
    for date in possible_birthdays:
        if date[1] == day:
            bag += (date[1],)
    if len(bag) >= 2:
        return False
    return True

def unique_month(month, possible_birthdays):
    bag = ()
    for date in possible_birthdays:
        if date[0] == month:
            bag += (date[0],)
    if len(bag) >= 2:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if date[0] == month:
            day = date[1]
            if unique_day(day, possible_birthdays):
                return True
            else:
                continue
    return False
