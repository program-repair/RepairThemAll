def unique_day(day, possible_birthdays):
    unique = 0
    for i in possible_birthdays:
        if i[1] == day:
            unique += 1
    if unique > 1:
        return False
    return True
    
def unique_month(month, possible_birthdays):
    unique = 0
    for i in possible_birthdays:
        if i[0] == month:
            unique += 1
    if unique > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    bd = ()
    tru = 0
    for i in possible_birthdays:
        if i[0] == month:
            bd += (i),
    for i in bd:
        if unique_day(i[1], possible_birthdays) == True:
            tru += 1
    if tru > 0:
        return True
    return False
