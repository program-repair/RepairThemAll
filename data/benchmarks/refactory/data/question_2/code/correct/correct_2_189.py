def unique_day(day, possible_birthdays):
    dates = map(lambda x: x[1], possible_birthdays)
    counter = 0
    for date in dates:
        if day == date:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    months = map(lambda x: x[0], possible_birthdays)
    counter = 0
    for i in months:
        if month == i:
            counter += 1
    if counter == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    days_in_month = map(lambda x: x[1] if x[0] == month else (), possible_birthdays)
    check = map(lambda x: unique_day(x, possible_birthdays), days_in_month)
    return True in check
