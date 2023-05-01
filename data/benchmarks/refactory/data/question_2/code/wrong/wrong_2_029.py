def unique_day(date, possible_birthdays):
    tpl = ()
    for i in possible_birthdays:
        tpl += (i[1],)
    if tpl.count(date) > 1:
        return False
    return True    

def unique_month(month, possible_birthdays):
    tpl = ()
    for j in possible_birthdays:
        tpl += (j[0],)
    if tpl.count(month) > 1:
        return False
    return True    

def contains_unique_day(month, possible_birthdays):
    tpl = ()
    for k in possible_birthdays:
        if k[0] == month:
            tpl += (k[1],)
    for l in tpl:
        if unique_day(l, possible_birthdays) == True:
            return True
    return False        
