def unique_day(day, possible_birthdays):
    all_days = ()
    repeat_days =()
    for date in possible_birthdays:
        if date[1] not in all_days:
            all_days += (date[1],)
        else:
            repeat_days += (date[1],)
    return day not in repeat_days   

def unique_month(month, possible_birthdays):
    all_month = ()
    repeat_month =()
    for date in possible_birthdays:
        if date[0] not in all_month:
            all_month += (date[0],)
        else:
            repeat_month += (date[0],)
    return month not in repeat_month 

def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if unique_day(date[1],possible_birthdays):
            if month == date[0]:
                return True
            else:
                continue
    else:
        return False
