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

def keep_month(month,possible_birthdays):
    new_list = ()
    for date in possible_birthdays:
        if month == date[0]:
            new_list = new_list + (date,)
    return new_list



def contains_unique_day(month, possible_birthdays):
    counter = 0
    revised_list = keep_month(month,possible_birthdays)
    for i in revised_list:
        if unique_day(i[1], possible_birthdays) == True:
            return True

    return False 
