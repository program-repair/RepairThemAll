def unique_day(day, possible_birthdays):
    possible_days = tuple(map(lambda x: x[1], possible_birthdays))
    if possible_days.count(day) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    possible_months = tuple(map(lambda x: x[0], possible_birthdays))
    if possible_months.count(month) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    #Gets the unique days in the form (month, days)
    unique_days = tuple(filter(lambda x: unique_day(x[1], possible_birthdays), possible_birthdays))
    for birthday in unique_days:
        if birthday[0] == month:
            return True
    return False
