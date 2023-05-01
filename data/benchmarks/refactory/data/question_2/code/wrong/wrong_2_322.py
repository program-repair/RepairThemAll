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
    counter=0
    for dates in possible_birthdays:
        if month==dates[0]:
            counter=counter+1
        else:
            continue
    if counter>1:
        return False
    else:
        return True 

def contains_unique_day(month, possible_birthdays):
    
    def month_tuple(month,possible_birthdays):
        new_tuple=()
        for dates in possible_birthdays:
            if month==dates[0]:
                new_tuple=new_tuple+(dates,)
            else:
                continue
        
        return new_tuple
    new_tuple=month_tuple(month,possible_birthdays)
    for dates2 in new_tuple:
        counter=0
        for dates in possible_birthdays:
            if dates2[1]==dates[1]:
                counter=counter+1
            else:
                continue
    if counter>1:
            return False
    else:
            return True
