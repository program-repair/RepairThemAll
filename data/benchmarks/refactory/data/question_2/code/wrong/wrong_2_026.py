def unique_day(day, possible_birthdays):
    checker = []
    for bday in possible_birthdays:
        if day == bday[1] and day not in checker:
            checker.append(day)
        elif day == bday[1] and day in checker:
            return False
    return True

def unique_month(month, possible_birthdays):
    checker = []
    for bday in possible_birthdays:
        if month == bday[0] and month not in checker:
            checker.append(month)
        elif month == bday[0] and month in checker:
            return False
    return True
    
def contains_unique_day(month, possible_birthdays):
    for bday in possible_birthdays:
        if bday[0] == month:
            if unique_day(bday[1], possible_birthdays) == True:
                return True
    return False
