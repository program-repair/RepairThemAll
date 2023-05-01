def unique_day(day, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[1]==day:
            counter=counter+1
    if counter<=1:
        return true
    else:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[0]==month:
            counter=counter+1
    if counter<=1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    temp=()
    for i in possible_birthdays:
        if i[0]==month:
            temp=temp+(i,)
    for i in temp:
        if unique_day(i[1],possible_birthdays):
            return True
    return False
