def unique_day(day, possible_birthdays):
       
    days = 0 
        
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            days = days + 1
            
    if days == 1:
        return True
    else:
        return False 
        


def unique_month(month, possible_birthdays):
    
    months = 0
    for j in range(len(possible_birthdays)):
        
        if possible_birthdays[j][0] == month:
            months = months + 1
    if months == 1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    
    x = () 
    
    for k in range(len(possible_birthdays)):
        
        if possible_birthdays[k][0] == month:
            
            x = x + (possible_birthdays[k],)
            
    for l in range(len(x)):
        if unique_day(x[l][1], possible_birthdays):
            return True
        else:
            continue
    return False 
