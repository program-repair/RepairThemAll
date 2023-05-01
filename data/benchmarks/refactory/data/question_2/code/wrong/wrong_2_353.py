def unique_day(date, possible_birthdays):
    lenth=len(possible_birthdays)
    count=0
    for i in range(0,lenth):
        if date==possible_birthdays[i][1]:
            count=count+1
    if count==1:
        return True
    else:
        return False
    

def unique_month(month, possible_birthdays):
    lenth=len(possible_birthdays)
    count=0
    for i in range(0,lenth):
        if month==possible_birthdays[i][0]:
            count=count+1
    if count==1:
        return True
    else:
        return False
    

def contains_unique_day(month, possible_birthdays):
    count=()
    for i in possible_birthdays:
        if i[0]==month:
            count=count+i
    for j in count:
        if unique_day(j[1], possible_birthdays):
            return True
        else:
            return False
