def unique_day(day, possible_birthdays):
    occurence = 0
    for date in possible_birthdays:
        if day == date[1]:
            occurence +=1
    if occurence == 0 or occurence > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    occurence = 0
    for date in possible_birthdays:
        if month == date[0]:
            occurence +=1
    if occurence == 0 or occurence > 1:
        return False
    return True 

def contains_unique_day(month, possible_birthdays):
    more_possible_dates = filter(lambda date: date[0] == month, possible_birthdays)
    for date in more_possible_dates:
        if unique_day(date[1], possible_birthdays):
            return True
    return False
