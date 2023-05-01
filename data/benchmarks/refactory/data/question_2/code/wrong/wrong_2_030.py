def unique_day(date, possible_birthdays):
    tpl = ()
    for i in possible_birthdays:
        tpl += (i[1],)
    if tpl.count(date) > 1:
        return False
    return True    

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
