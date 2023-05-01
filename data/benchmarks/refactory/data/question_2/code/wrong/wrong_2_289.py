def unique_day(date, possible_birthdays):
    a = ()
    for i in possible_birthdays:
        a += (i[1],)
    return a.count(day) == 1

def unique_month(month, possible_birthdays):
    a = ()
    for i in possible_birthdays:
        a += (i[1],)
    return a.count(month) == 1
    
def contains_unique_day(month, possible_birthdays):
    a = ()
    b = False
    for i in possible_birthdays:
        if month == i[0]:
            a += (i,)
    for i in a:
        b = b or unique_day(i[1], possible_birthdays)
    return b
