def unique_day(day, possible_birthdays):
    count = 0
    for item in possible_birthdays:
        if day == item[1]:
            count +=1
        else:
            continue
    if count >=2:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    count = 0
    for item in possible_birthdays:
        if month == item[0]:
            count +=1
        else:
            continue
    if count >=2:
        return False
    else:
        return True


def contains_unique_day(month, possible_birthdays):
    day = filter(lambda x: x[0]== month, possible_birthdays)
    for item in tuple(day):
        if unique_day(item[1],possible_birthdays) == True:
            return True
        else:
            continue
    return False 
