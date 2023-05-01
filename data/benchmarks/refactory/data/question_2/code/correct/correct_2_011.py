def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if day in i:
            counter += 1
    return counter == 1

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if month in i:
            counter += 1
    return counter == 1

def contains_unique_day(month, possible_birthdays):
    daysinmonth =()
    for i in possible_birthdays:
        if month in i:
            daysinmonth += (i[1],)
    for j in daysinmonth:
        if unique_day(j, possible_birthdays):
            return True   
    return False 
