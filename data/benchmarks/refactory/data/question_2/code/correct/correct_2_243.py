def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            counter = counter + 1
    if counter != 1:
        return False
    return True
    
def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            counter = counter + 1
    if counter != 1:
        return False
    return True
    
def contains_unique_day(month, possible_birthdays):
    count_of_days = ()
    for i in possible_birthdays:
        if month == i[0]:
            count_of_days = count_of_days + (i[1], )
    for i2 in count_of_days:     
        if unique_day(i2, possible_birthdays) == True:
            return True
    return False
