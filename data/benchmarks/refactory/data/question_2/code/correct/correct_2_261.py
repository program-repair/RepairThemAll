
def unique_day(day, possible_birthdays):
    counter = 0
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    total,i = (), 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][0] == month:
            total += (possible_birthdays[i],)
        i += 1
    for x in total:
        if unique_day(x[1], possible_birthdays) == True:
            return True
    return False
