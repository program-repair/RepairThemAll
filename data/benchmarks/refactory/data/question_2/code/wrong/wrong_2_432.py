def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == date:
            counter += 1
    if counter > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[0] == month:
            counter += 1
    if counter > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    new_tuple = ()
    for i in possible_birthdays:
        if i[0] == month:
            new_tuple += (i,)
        if len(new_tuple)>1:
            return False
        else:
            return unique_day(new_tuple[0][1], possible_birthdays)
