def unique_day(day, possible_birthdays):
    counter = 0
    result = 0
    while counter < len(possible_birthdays):
        date = possible_birthdays[counter][1]
        if date == day:
            result = result + 1
        counter = counter + 1
    if result > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    result = 0
    while counter < len(possible_birthdays):
        chosen_month = possible_birthdays[counter][0]
        if chosen_month == month:
            result = result + 1
        counter = counter + 1
    if result > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    counter = 0
    while counter < len(possible_birthdays):
        get_month = possible_birthdays[counter][0]
        if get_month == month:
            test_date = possible_birthdays[counter][1]
            if unique_day(test_date, possible_birthdays) == True:
                return True
        counter = counter + 1
    return False 
