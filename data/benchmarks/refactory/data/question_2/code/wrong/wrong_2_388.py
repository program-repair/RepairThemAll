def unique_day(day, possible_birthdays):
    count = 0
    for month_day in possible_birthdays:
        date = month_day[1]
        if day == date:
            count+= 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for month_day in possible_birthdays:
        mont = month_day[0]
        if month == mont:
            count+= 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    condition = False
    for month_day in possible_birthdays:
        if month == month_day[0]:
            condition = unique_day(month_day[1],possible_birthdays)
    return condition
