def unique_day(date, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if date in i:
            counter +=1
    if counter >1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month in i:
            counter += 1
    if counter > 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    birthdays = ()
    for i in possible_birthdays:
        if month in i:
            birthdays += (i,)
    for i in birthdays:
        if not unique_day(i[1], possible_birthdays):
            result = False
        else:
            result = True
            break
    return result
