def unique_day(day, possible_birthdays):
    day_count = 0
    for i in possible_birthdays:
        if day in i:
            day_count += 1
        if day_count > 1:
            return False
    if day_count == 0:
        return False   
    return True


def unique_month(month, possible_birthdays):
    month_count = 0
    for i in possible_birthdays:
        if month in i:
            month_count += 1
        if month_count > 1:
            return False
    if month_count == 0:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    days_in_month = ()
    for i in possible_birthdays:
        if month in i:
            days_in_month += (i[1],)
    for i in days_in_month:
        if unique_day(i, possible_birthdays):
            return True
    return False
