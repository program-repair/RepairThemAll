def unique_day(day, possible_birthdays):
    """Your solution here"""
    a = 0
    for birthday in possible_birthdays:
        if birthday[1] == day:
            a = a + 1
    if a == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    """Your solution here"""
    a = 0
    for birthday in possible_birthdays:
        if birthday[0] == month:
            a = a + 1
    if a == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    """Your solution here"""
    b = False
    def month_tup(month):
        a = ()
        for birthday in possible_birthdays:
            if month == birthday[0]:
                a = a + (birthday,)
        return a
    for birthday in month_tup(month):
        if unique_day(birthday[1], possible_birthdays) == True:
            b = True
    return b
