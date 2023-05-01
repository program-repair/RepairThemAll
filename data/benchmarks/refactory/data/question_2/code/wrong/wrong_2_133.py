def unique_day(day, possible_birthdays):
    unique_day_counter = 0
    for i in possible_birthdays:
        if day == i[1]:
            unique_day_counter += 1
    if unique_day_counter != 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    unique_month_counter = 0
    for i in possible_birthdays:
        if month == i[0]:
            unique_month_counter += 1
    if unique_month_counter != 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    return 
