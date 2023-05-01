def unique_day(day, possible_birthdays):
    count = 0
    for x in possible_birthdays:
        if day in x:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for x in possible_birthdays:
        if month in x:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    possible_days = ()
    for x in possible_birthdays:
        if month in x:
            possible_days += (x[1],)
    for x in possible_days:
        contains = unique_day(x,possible_birthdays)
        if contains == False:
            continue
        else:
            return True
    return False
