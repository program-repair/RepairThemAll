def unique_day(day, possible_birthdays):
    n = len(possible_birthdays)
    result = 0
    for counter in range(n):
        if day == possible_birthdays[counter][1]:
            result = result + 1
    return result == 1

def unique_month(month, possible_birthdays):
    n = len(possible_birthdays)
    result = 0
    for counter in range(n):
        if month == possible_birthdays[counter][0]:
            result = result + 1
    return result == 1

def contains_unique_day(month, possible_birthdays):
    n = len(possible_birthdays)
    for counter in range(n):
        if month == possible_birthdays[counter][0]:
            if unique_day(possible_birthdays[counter][1], possible_birthdays) == True:
                return True
    return False
