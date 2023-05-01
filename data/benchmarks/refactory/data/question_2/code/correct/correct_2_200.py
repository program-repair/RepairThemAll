def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            count+=1
    if count==1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
                count+=1
    if count==1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    days=()
    for birthday in possible_birthdays:
        if month== birthday[0]:
            days += (birthday[1],)
    for day in days:
        if unique_day(day, possible_birthdays)== False:
            continue
        else:
            return unique_day(day, possible_birthdays)
    return False
