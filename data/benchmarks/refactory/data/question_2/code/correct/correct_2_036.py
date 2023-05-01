def unique_day(day, possible_birthdays):
    result = 0
    for bday in possible_birthdays:
        if bday[1] == day:
            result += 1
    return result == 1
def unique_month(month, possible_birthdays):
    result = 0
    for bday in possible_birthdays:
        if bday[0] == month:
            result += 1
    return result == 1
def contains_unique_day(month, possible_birthdays):
    filter_month = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for day in filter_month:
        if unique_day(day[1], possible_birthdays):
            return True
    return False
