def unique_day(day, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            count += 1
    return True if count == 1 else False
    
def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            count += 1
    return True if count == 1 else False

def contains_unique_day(month, possible_birthdays):
    tup = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            tup += (birthday,)
    for each in tup:
        if each[1] == '18' or each[1] == '19':
            return True
    return False 
