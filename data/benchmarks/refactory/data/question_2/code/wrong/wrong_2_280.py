def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    focus = ()
    unique_days = ()
    for i in possible_birthdays:
        if month == i[0]:
            focus += (i,)
    for j in focus:
        testday = j[1]
        if unique_day(testday, possible_birthdays) == True:
            unique_days += (testday,)
    for k in unique_days:
        for l in focus:
            if k == l[1]:
                break
            return True
    return False
