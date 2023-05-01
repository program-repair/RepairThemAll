def unique_day(day, possible_birthdays):
    days = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(days) <= 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    months = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(months) <= 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    dates = ()
    for date in possible_birthdays:
        if date[0] == month:
            dates += (date,)
    for dated in dates:
        if unique_day(dated[1], possible_birthdays) == True:
            return True
    else:
        return False
