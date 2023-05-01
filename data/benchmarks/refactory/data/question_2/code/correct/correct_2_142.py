def unique_day(day, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if i[1] == day:
            result += 1
        elif i[1] != day:
            result += 0
    if result == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    result = 0
    for i in possible_birthdays:
        if i[0] == month:
            result += 1
        elif i[0] != month:
            result += 0
    if result == 1:
        return True
    else:
        return False


def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(i[1],possible_birthdays):
                return True
            else:
                continue
        else:
            continue
    return False

