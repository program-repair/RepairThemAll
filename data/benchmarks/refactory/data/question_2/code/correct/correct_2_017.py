def unique_day(day, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count += 1
    if count == 1:
        return True
    else:
        return False
        
def unique_month(month, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count += 1
    if count == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    for date in possible_birthdays:
        if unique_day(date[1], possible_birthdays) == True and month == date[0]:
            return True
    return False       
