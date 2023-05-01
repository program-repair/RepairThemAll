def unique_day(day, possible_birthdays):
    n=0
    for tup in possible_birthdays:
        if tup[1]==day:
            n+=1
    if n==1:
        return True           
    return False
    
def unique_month(month, possible_birthdays):
    n=0
    for tup in possible_birthdays:
        if tup[0]==month:
            n+=1
    if n==1:
        return True           
    return False
    
    
def contains_unique_day(month, possible_birthdays):
    n=0
    for tup in possible_birthdays:
        if tup[0]==month:
            if unique_day(tup[1],possible_birthdays):
                n+=1
    if n>=1:
        return True
    return False
