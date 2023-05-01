def unique_day(day, possible_birthdays):
    counter = 0
    for dates in possible_birthdays:
        if day == dates[1]:
            possible_birthdays = possible_birthdays[1:]
            counter = counter + 1 
    if counter == 1:
        return True
    else:
        return False 
    return

def unique_month(month, possible_birthdays):
    counter = 0
    for dates in possible_birthdays:
        if month == dates[0]:
            possible_birthdays = possible_birthdays[1:]
            counter = counter + 1 
    if counter == 1:
        return True
    else:
        return False 

def contains_unique_day(month, possible_birthdays):
    counter = 0
    new_list = keep_month(month,possible_birthdays)
    for i in new_list:
        if unique_day(i[1], possible_birthdays) == True:
            return True

    return False 
