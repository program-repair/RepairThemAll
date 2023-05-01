def unique_day(day, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        birthday = i[1]
        if day == birthday:
            count = count + 1
        else:
            count = count
    if count > 1:
        return False
    elif count <= 1:
        return True

def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        birthday = i[0]
        if month == birthday:
            count = count + 1
        else:
            count = count
    if count > 1:
        return False
    elif count <= 1:
        return True

def contains_unique_day(month, possible_birthdays):
    tup_month_1 = ()
    tup_month_2 = ()
    for i in possible_birthdays:
        if month == i[0]:
            tup_month_1 = tup_month_1 + (i,)
        else:
            tup_month_2 = tup_month_2 + (i[1],)
    for j in tup_month_1:
        day = j[1]
        if day in tup_month_2:
            continue
        elif day not in tup_month_2:
            return True
    else:
        return False
