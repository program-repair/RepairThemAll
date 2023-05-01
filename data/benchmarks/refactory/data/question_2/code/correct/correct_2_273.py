def unique_day(day, possible_birthdays):
    
    if len(tuple(filter(
        lambda x : x[1] == day, possible_birthdays))) == 1:
        return True
    return False

def unique_month(month, possible_birthdays):

    if len(tuple(filter(
        lambda x : x[0] == month, possible_birthdays))) == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    special_days = tuple(filter((
        lambda x: unique_day(x[1], possible_birthdays)),
                                possible_birthdays))
    for i in special_days:
        if i[0] == month:
            return True
    return False
