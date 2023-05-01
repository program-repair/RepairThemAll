def unique_day(day, possible_birthdays):
    the_day = ()
    for i in possible_birthdays:
        if i[1] == day:
            the_day += (day,)
    return len(the_day) == 1

def unique_month(month, possible_birthdays):
    the_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            the_month += (month,)
    return len(the_month) == 1

def contains_unique_day(month, possible_birthdays):
    return 
