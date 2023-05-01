def unique_day(day, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if day == date[1]:
            counter+=1
    return counter==1

def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if month == date[0]:
            counter+=1
    return counter==1

def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if month==date[0]:
            if unique_day(date[1], possible_birthdays):
                return True
    return False
