def unique_day(day, possible_birthdays):
    all_days = ()
    for i in possible_birthdays:
        all_days += (i[1],)
    return all_days.count(day) == 1

def unique_month(month, possible_birthdays):
    all_months = ()
    for i in possible_birthdays:
        all_months += (i[0],)
    return all_months.count(month) == 1

def contains_unique_day(month, possible_birthdays):
    all_day_in_given_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            all_day_in_given_month += (i[1],)
    for i in all_day_in_given_month:
        if unique_day(i, possible_birthdays):
            return True
    return False
