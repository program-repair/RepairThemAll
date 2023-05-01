def unique_day(day, possible_birthdays):
    freq=0
    for birthday in possible_birthdays:
        if birthday[1]==day:
            freq=freq+1
        else:
            continue
    if freq==1:
        return True
    else:
        return False


def unique_month(month, possible_birthdays):
    freq=0
    for birthday in possible_birthdays:
        if birthday[0]==month:
            freq=freq+1
        else:
            continue
    if freq==1:
        return True
    else:
        return False


def contains_unique_day(month, possible_birthdays):
    for birthday in possible_birthdays:
        if birthday[0]==month:
            if unique_day(birthday[1], possible_birthdays)==True:
                return True
                break
        
    return False
        
