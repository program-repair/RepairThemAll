def unique_day(day, possible_birthdays):
    b=[]  # list of dates
    for birthday in possible_birthdays:
        b.append(birthday[1])
    if b.count(day)==1:
        return True
    
    return False

def unique_month(month, possible_birthdays):
    b=[] 
    for birthday in possible_birthdays:
        b.append(birthday[0])
    if b.count(month)==1:
        return True
    
    return False
    
def contains_unique_day(month, possible_birthdays):
    b=[]
    for birthday in possible_birthdays:
        if month == birthday[0]:
            b.append(birthday[1])  #add date to b
    for day in b:
        if unique_day(day,possible_birthdays)==True:
            return True
    
    return False
