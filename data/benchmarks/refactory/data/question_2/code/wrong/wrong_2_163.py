def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if i[1]==day:
            count+=1
    if count>1:
        check=False
    else:
        check=True
    return check

def unique_month(month, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if i[0]==month:
            count+=1
    if count>1:
        check=False
    else:
        check=True
    return check


def contains_unique_day(month, possible_birthdays):
    birthdays=()
    for i in possible_birthdays:
        if i[0]==month:
            birthdays+=(i,)
    for j in birthdays:
        if unique_day(j[1], possible_birthdays):
            return True
    return False
            
