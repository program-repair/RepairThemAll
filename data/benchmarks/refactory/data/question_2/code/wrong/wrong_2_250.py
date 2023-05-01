def unique_day(day, possible_birthdays):
    value = 0
    for i in range(0, len(possible_birthdays)):
        if (day == possible_birthdays[i][1]):
            value += 1
    if (value > 1) or (value == 0):
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
