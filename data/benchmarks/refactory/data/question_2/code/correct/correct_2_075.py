def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day in i:
            counter += 1
    return True if counter == 1 else False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month in i:
            counter += 1
    return True if counter == 1 else False

def contains_unique_day(month, possible_birthdays):
    counter = 0
    result = False
    for i in possible_birthdays:
        if month == i[0]:
            result = result or unique_day(i[1], possible_birthdays)
    return result
