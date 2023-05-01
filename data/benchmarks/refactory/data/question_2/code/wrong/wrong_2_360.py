def unique_day(day, possible_birthdays):
    count = ()
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count = count + (possible_birthdays[i][1],)
    if len(count) < 2:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count = ()
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count = count + (possible_birthdays[i][0],)
    if len(count) < 2:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    count = ()
    result = ()
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count = count + (possible_birthdays[i][1],)
            for j in count:
                result = result + (unique_day(j, possible_birthdays),)
    if True in result:
        return True
    else:
        return False
