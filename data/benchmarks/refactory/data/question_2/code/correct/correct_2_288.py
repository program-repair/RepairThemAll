def unique_day(day, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[1]==day:
            counter+=1
    return counter==1
    
def unique_month(month, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[0]==month:
            counter+=1
    return counter==1
    
def contains_unique_day(month, possible_birthdays):
    value=()
    for i in possible_birthdays:
        if i[0]==month:
            value+=(i,)
    for i in value:
        if unique_day(i[1],possible_birthdays):
            return True
    return False
