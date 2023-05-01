def unique_day(date, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if day == bday[1]:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for bday in possible_birthdays:
        if month == bday[0]:
            count += 1
    return count == 1

def contains_unique_day(month, possible_birthdays):
    for bday in possible_birthdays:
        if month == bday[0]:
            if unique_day(bday[1], possible_birthdays):
                return True
    return False 
