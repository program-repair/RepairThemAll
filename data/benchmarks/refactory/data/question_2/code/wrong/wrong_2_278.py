def unique_day(day, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count += 1
    if count > 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    for day in possible_birthdays:
        if unique_day(day[1], possible_birthdays) == True and month == day[0]:
            return True
        else:
            return False
