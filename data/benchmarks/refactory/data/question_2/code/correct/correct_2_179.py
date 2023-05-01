
def unique_day(day, possible_birthdays):
    if len(tuple(filter(lambda x: x[1] == day, possible_birthdays))) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    if len(tuple(filter(lambda x: x[0] == month, possible_birthdays))) == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    total = ()
    i = 0
    while i < len(possible_birthdays):
        if possible_birthdays[i][0] == month:
            total = total + (possible_birthdays[i],)
        else:
            total = total
        i = i + 1
    for t in total:
        if unique_day(t[1], possible_birthdays) == True:
            return True
    return False
