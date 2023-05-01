def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            counter = counter + 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            counter = counter + 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    tup = ()
    for i in possible_birthdays:
        if month == i[0]:
           tup = tup + (i,)
    for j in tup:
        day = j[1]
        if unique_day(day, possible_birthdays) == True:
            return True
    else:
        return False
