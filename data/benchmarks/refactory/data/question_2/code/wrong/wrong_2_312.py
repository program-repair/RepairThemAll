def unique_day(day, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if date[1]==day:
            conter+=1
        else:
            counter=counter
    if counter==1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if date[1]==month:
            conter+=1
        else:
            counter=counter
    if counter==1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    return 
