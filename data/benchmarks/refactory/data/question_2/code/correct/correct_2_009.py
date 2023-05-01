def unique_day(day, possible_birthdays):
    return tuple(map(lambda x: x[1], possible_birthdays)).count(day) == 1

def unique_month(month, possible_birthdays):
    return tuple(map(lambda x: x[0], possible_birthdays)).count(month) == 1

def contains_unique_day(month, possible_birthdays):
    is_unique_day = tuple((i, unique_day(i, possible_birthdays)) for i in tuple(map(lambda y: y[1], possible_birthdays)))
    is_unique_day_true = tuple(map(lambda c: c[0], tuple(filter(lambda b: b[1] == True, is_unique_day))))
    days_in_month = tuple(map(lambda b: b[1], tuple(filter(lambda d: d[0] == month, possible_birthdays))))
    check_month = tuple(x in days_in_month for x in is_unique_day_true)
    return True in check_month
