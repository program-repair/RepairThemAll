def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if day == i[1]:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if month== i[0]:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
def contains_unique_day(month, possible_birthdays):
    newtuple = ()
    for i in possible_birthdays:
        if month== i[0]:
            newtuple = newtuple + (i,)
    for j in newtuple:
        if unique_day(j[1], possible_birthdays) == True:
            return True
    else:
        return False
