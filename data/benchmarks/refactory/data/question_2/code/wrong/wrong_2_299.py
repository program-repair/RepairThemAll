def unique_day(day, possible_birthdays):
    counter=0
    for dates in possible_birthdays:
        if day==dates[1]:
            counter=counter+1
        else:
            continue
    if counter>1:
        return False
    else:
        return True 
    

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
