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
    value = 0
    for i in range(0, len(possible_birthdays)):
        if (month == possible_birthdays[i][0]):
            value += 1
    if (value > 1) or (value == 0):
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    unique_days = ()
    for i in range(0, len(possible_birthdays)):
        if (unique_day(possible_birthdays[i][1], possible_birthdays) == True):
            unique_days += (possible_birthdays[i][1],)
    for j in range(0, len(unique_days)):
        if ((month, unique_days[j]) in possible_birthdays):
            return True
    return False  
