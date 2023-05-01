def unique_day(day, possible_birthdays):
    a=0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            a = a + 1
    if a == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    a=0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            a = a + 1
    if a == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    x = ()
    for birthday in possible_birthdays:
        mn,dy = birthday
        if mn == month:
            x = x + (dy,)
    for i in x:
        if unique_day(i,possible_birthdays) == True:
            return True
    return False
