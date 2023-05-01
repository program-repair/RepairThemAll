def unique_day(day, possible_birthdays):
    result = 0
    for i in range(len(possible_birthdays)):
        if day in possible_birthdays[i]:
            result += 1
    if result == 1:
        return True
    else:
        return False


def unique_month(month, possible_birthdays):
    result = 0
    for i in range(len(possible_birthdays)):
        if month in possible_birthdays[i]:
            result += 1
    if result == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    days = ()
    for i in possible_birthdays:
        if i[0] == month:
            days += (i[1],)
    for i in days:
        if unique_day(i, possible_birthdays):
            return True
    return False
