def unique_day(day, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        if day == x[1]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for x in possible_birthdays:
        if month == x[0]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    temp = [x for x in possible_birthdays if x[0] == month]
    temp = tuple(temp)
    counter = 0
    for x in temp:
        if unique_day(x[1], possible_birthdays):
            counter += 1
    if counter > 0:
        return True
    else:
        return False
