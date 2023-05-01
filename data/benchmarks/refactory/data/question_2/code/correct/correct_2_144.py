def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False
        
def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            counter += 1
        else:
            continue
    if counter == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    counter = 0
    dummy = ()
    indicator = ()
    for i in possible_birthdays:
        if month == i[0]:
            dummy += (i,)
    for i in dummy:
        indicator += (unique_day(i[1],possible_birthdays),)
    if True not in indicator:
        return False
    else:
        return True
