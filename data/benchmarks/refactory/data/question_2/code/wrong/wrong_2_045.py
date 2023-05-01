
def unique_day(day, possible_birthdays):
    
    count=0
    for birthday in possible_birthdays:
        if day in birthday[1]:
            count+=1
    if count==1:
        return True
    else:
        return False    


def unique_month(month, possible_birthdays):
    count=0
    for birthday_month in possible_birthdays:
        if month in birthday_month[0]:
            count+=1
    if count==1:
        return True
    else:
        return False
 


def contains_unique_day(month, possible_birthdays):
    month_tuple=()
    for birthday in possible_birthdays:
        if month==birthday[0]:
            month_tuple+=(birthday,)
        else:
            continue
    for day in month_tuple:
        
        if unique_day(day[1], possible_birthdays)== True :
            return True
    return False
    
