def unique_day(day, possible_birthdays):
    count_day = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            if count_day == 0: count_day += 1
            else: return False
    return True

def unique_month(month, possible_birthdays):
    count_month = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            if count_month == 0: count_month += 1
            else: return False
    return True

def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if month == birthday[0]:
            day = birthday[1]
            if unique_day(day, possible_birthdays): return True
    return False
