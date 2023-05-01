def unique_day(date, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            count = count + 1
    if count>1:
        return False
    else:
        return True    

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            count = count + 1
    if count>1:
        return False
    else:
        return True


def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if month == birthday[0]:
            if unique_day(birthday[1], possible_birthdays) == True:
               return True
    return False
          
