def unique_day(day, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if day in date:
            counter+=1
    if counter>1:
        return False 
    return True


def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if month in date:
            counter+=1
        if counter>1:
            return False 
    return True

def contains_unique_day(month, possible_birthdays):
    dates=()
    for date in possible_birthdays:
        months,day=date
        if unique_day(day, possible_birthdays):
            dates+=(months,)
    return month in dates
