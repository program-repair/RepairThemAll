def unique_day(day, possible_birthdays):
    i, times = 0, 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][1] == day:
            times += 1
        i += 1
    if times == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    i, times = 0, 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][0] == month:
            times += 1
        i += 1
    if times == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for i in range (0,len(possible_birthdays)):
        if possible_birthdays[i][0] == month and unique_day(possible_birthdays[i][1], possible_birthdays):
            return True
    else:
        return False
