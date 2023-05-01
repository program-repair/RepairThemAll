def unique_day(date, possible_birthdays):
       
    days = 0 
        
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == days:
            day = day + 1
            
    if days == 1:
        return True
    else:
        return False 

def unique_month(month, possible_birthdays):
    
    month = 0
    
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0] == days:
            day = day + 1
            
    if days == 1:
        return True
    else:
        return False 
        
def contains_unique_day(month, possible_birthdays):
    
    x = () 
    
    for i in range(len(possible_birthdays)):
        
        if possible_birthdays[i][0] == month:
            
            x = x + (possible_birthdays[i],)
    for j in range(len(x)):
        if unique_day(x[j][1], possible_birthdays):
            return True
        else:
            continue
    return False 
