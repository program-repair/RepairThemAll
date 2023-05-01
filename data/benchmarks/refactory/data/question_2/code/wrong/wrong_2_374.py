def unique_day(day, possible_birthdays):
    datetup = ()
    for item in possible_birthdays:
        if item[1] == day:
            datetup = datetup + (item[1],)
    if len(datetup) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
