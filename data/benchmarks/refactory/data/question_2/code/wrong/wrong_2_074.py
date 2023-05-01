def unique_day(date, possible_birthdays):
    no_of_days = 0
    for i in possible_birthdays:
        if i[1] == day:
            no_of_days += 1
    if no_of_days != 1:
        return False
    return True
    
def unique_month(month, possible_birthdays):
    no_of_months = 0
    for i in possible_birthdays:
        if i[0] == month:
            no_of_months += 1
    if no_of_months != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    birthdays_with_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            birthdays_with_month += (i[1],)
    counter = 0
    for i in birthdays_with_month:
        if unique_day(i, possible_birthdays) == True:
            counter += 1
    if counter == 1:
        return True
    else:
        return False 
