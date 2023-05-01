def unique_day(day, possible_birthdays):
    get_possible_days = map(lambda bdays:bdays[1],possible_birthdays)
    count = 0
    for days in get_possible_days:
        if days == day:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
def unique_month(month, possible_birthdays):
    get_possible_months = map(lambda bdays:bdays[0],possible_birthdays)
    count = 0
    for months in get_possible_months:
        if months == month:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
def contains_unique_day(month, possible_birthdays):
     get_possible_months = filter(lambda birthday: birthday[0] == month, possible_birthdays)
     get_possible_days = map(lambda birthday: birthday[1],get_possible_months)
     for days in get_possible_days:
        if unique_day(days, possible_birthdays):
            return True
     return False
