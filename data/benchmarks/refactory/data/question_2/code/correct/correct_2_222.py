def unique_day(day, possible_birthdays):
    count=0
    for x in possible_birthdays:
        if x[1]==day:
            count=count+1
    if count == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    count=0
    for x in possible_birthdays:
        if x[0]==month:
            count=count+1
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for x in possible_birthdays:
        if x[0]==month:
            if unique_day(x[1], possible_birthdays):
                return True
            else:
                continue
        else:
            continue
    return False
    
