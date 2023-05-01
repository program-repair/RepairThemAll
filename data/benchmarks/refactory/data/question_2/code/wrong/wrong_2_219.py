def unique_day(date, possible_birthdays):
    j = 0
    for i in possible_birthdays:
        if date == i[1]:
            j = j+1
        else:
            j = j
    if j == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
