def unique_day(day, possible_birthdays):
    count = 0
    alldays = ()
    for i in possible_birthdays:
        alldays += (i[1],)
    for i in alldays:
        if day == i:
            count += 1
    if count == 1:
        return True
    else:
        return False
        
def unique_month(month, possible_birthdays):
    count = 0
    allmonths = ()
    for i in possible_birthdays:
        allmonths += (i[0],)
    for i in allmonths:
        if month == i:
            count += 1
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    count = 0
    matchmonth = ()
    for i in possible_birthdays:
        if month == i[0]:
            matchmonth += (i,)
    for i in matchmonth:
        if unique_day(i[1], possible_birthdays):
            return True
    return False
