def unique_day(day, possible_birthdays):
    count = 0
    for date in possible_birthdays:
        if date[1] == day:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for mon in possible_birthdays:
        if date[0] == month:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    return 
