def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day in i:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month in i:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    new_list = ()
    for i in possible_birthdays:
        if month in i:
            new_list += (i,)
    if len(new_list)== 1 or 0:
        return False
    else:
        counter = 0
        for i in new_list:
            if unique_day(i[1], possible_birthdays) == True:
                counter += 1
        if counter >= 1:
            return True
        else:
            return False
