def unique_day(day, possible_birthdays):
    counter = 0
    for j in possible_birthdays:
        if day == j[1]:
            counter += 1
    if counter != 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    counter = 0
    for j in possible_birthdays:
        if month == j[0]:
            counter +=1
    if counter != 1:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    for j in possible_birthdays:
        if month != j[0]:
            continue
        else:
            if unique_day(j[1],possible_birthdays):
                return True
    return False

