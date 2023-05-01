def unique_day(day, possible_birthdays):
    a = 0
    for item in possible_birthdays:
        for i in item:
            if i == day:
                a += 1
    if a == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    a = 0
    for item in possible_birthdays:
        for i in item:
            if i == month:
                a += 1
    if a == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    a = 0
    b = 0
    for item in possible_birthdays:
        if month in item:
            a = item
            if unique_day(item[1],possible_birthdays) == True:
                b += 1
    if b == 1:
        return True
    else:
        return False
