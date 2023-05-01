def unique_day(day, possible_birthdays):
    count = tuple(filter(lambda x: x[1] == day, possible_birthdays))
    if len(count) == 1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    if len(count) == 1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    T_or_F = False
    for i in possible_birthdays:
        if i[0] == month and unique_day(i[1], possible_birthdays):
            T_or_F = T_or_F or True
    return T_or_F
