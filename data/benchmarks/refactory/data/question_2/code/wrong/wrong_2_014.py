def unique_day(date, possible_birthdays):
    count = 0 
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            count += 1
    if count == 1:
        return True
    else:
        return False
        


def unique_month(month, possible_birthdays):
    
    months = 0
    for i in range(len(possible_birthdays)):
        
        if possible_birthdays[i][0] == month:
            months = months + 1
    if months == 1:
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
