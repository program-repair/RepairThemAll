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
    month_day = ()
    for j in possible_birthdays:
        if j == possible_birthdays[0]:
            month_day = month_day + (j,)
    for t in month_day:
        return unique_day(t[1], month_day)
