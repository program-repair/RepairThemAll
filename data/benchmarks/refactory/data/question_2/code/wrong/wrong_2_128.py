def unique_day(date, possible_birthdays):
    count = 0
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            count +=1
    if count == 1:
        return True
    else:
        return False 

def unique_month(month, possible_birthdays):
    count = 0
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            count +=1
    if count == 1:
        return True
    else:
        return False 

def contains_unique_day(month, possible_birthdays):
    return 
