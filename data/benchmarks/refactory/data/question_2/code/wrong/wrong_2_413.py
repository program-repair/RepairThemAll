def unique_day(day, possible_birthdays):
    for x in possible_birthdays:
        if day in x:
            return True
        else:
            return False

def unique_month(month, possible_birthdays):
    for dates in possible_birthdays:
        if month in dates:
            return False
        else:
            return True


def contains_unique_day(month, possible_birthdays):
    return 
