def unique_day(date, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            count += 1
    if count == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            count += 1
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == month and unique_day(possible_birthdays[i][1], possible_birthdays) == True:
            return True
    return False
