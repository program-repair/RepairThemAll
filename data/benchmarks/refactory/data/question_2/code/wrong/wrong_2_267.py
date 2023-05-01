def unique_day(day, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        check = possible_birthdays[i][1]
        if check == day:
            count = count+1
    if count >1:
        return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for i in range(len(possible_birthdays)):
        check = possible_birthdays[i][0]
        if check == month:
            count = count+1
    if count >1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    for i in range(len(possible_birthdays)):
        if month == possible_birthdays[i][0]:    
            day = possible_birthdays[i][1]
            check = unique_day(day, possible_birthdays)
            if check == True:
                return True
    return False
