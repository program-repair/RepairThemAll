def unique_day(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[1] == date:
            count = count + 1
    if count == 1:
        return True 
    else:
        return False

def unique_month(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            count = count + 1
    if count == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    same_month_tuple = ()
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            same_month_tuple = same_month_tuple + (i,)
    for i in same_month_tuple:
        if unique_day(i[0], possible_birthdays):
            return True
    return False
