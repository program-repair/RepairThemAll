def unique_day(day, possible_birthdays):
    counter = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[1] == day:
            counter += 1
    if counter > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for possible_birthday in possible_birthdays:
        if possible_birthday[0] == month:
            counter += 1
    if counter > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    filtered_birthdays = tuple(filter(lambda x: x[0] == month,possible_birthdays))
    for day in tuple(map(lambda x: x[1], filtered_birthdays)):
        if unique_day(day, possible_birthdays):
            return True
    return False
