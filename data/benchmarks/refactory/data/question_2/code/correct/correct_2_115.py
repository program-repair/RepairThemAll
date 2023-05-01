def unique_day(day, possible_birthdays):
    product = 0
    for i in possible_birthdays:
        if i[1] == day:
            product +=1
    if product == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    product = 0
    for i in possible_birthdays:
        if i[0] == month:
            product +=1
    if product == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month and unique_day(i[1], possible_birthdays) == True:
            return True
    else:
        return False
