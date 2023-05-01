def unique_day(date, possible_birthdays):
    count = 0
    for tup in possible_birthdays:
        if tup[1] == date:
            count+=1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for tup in possible_birthdays:
        if tup[0] == month:
            count+=1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    month_tup = ()
    for tup in possible_birthdays:
        if month in tup:
            month_tup += (tup,)
    for tup in month_tup:
        if unique_day(tup[1],possible_birthdays):
            return True
    return False
