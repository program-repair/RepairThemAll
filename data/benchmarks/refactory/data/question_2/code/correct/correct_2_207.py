def unique_day(day, possible_birthdays):
    count, result = 0, 0
    for count in range(0, len(possible_birthdays)):
        if day == possible_birthdays[count][1]:
            result = result + 1
        else:
            continue
    if result == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count, result = 0, 0
    for count in range(0, len(possible_birthdays)):
        if month == possible_birthdays[count][0]:
            result = result + 1
        else:
            continue
    if result == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for day in possible_birthdays:
        if month == day[0]:
            if unique_day(day[1], possible_birthdays):
                return True
        else:
            continue
    return False
