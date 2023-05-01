def unique_day(day, possible_birthdays):
    a  = 0
    for date in possible_birthdays:
        cb = date[1]
        if day == cb:
            a+= 1
        else:
            continue
    if a==1:
        return True
    else:
        return False
def unique_month(month, possible_birthdays):
    a = 0
    for date in possible_birthdays:
        lj = date[0]
        if month == lj:
           a+= 1
        else:
            continue
    if a == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    #find the possible days in that month
    #determine if they are unique days one by one
    possible_days = ()
    for date in possible_birthdays:
        if month == date[0]:
            possible_days += (date[1],)
        else:
            continue
    for day in possible_days:
        if unique_day(day,possible_birthdays):
            return True
        else:
            continue
    return False
