def unique_day(date, possible_birthdays):
    counter = 0
    for i in range(0,len(possible_birthdays)):
        if possible_birthdays[i][1] == date:
            counter = counter + 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
