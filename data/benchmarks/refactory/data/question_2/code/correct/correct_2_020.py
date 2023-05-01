def unique_day(day, possible_birthdays):
       
    days = 0 
        
    for i in range(len(possible_birthdays)): #creating the for loop for the range of possible birthdays
        if possible_birthdays[i][1] == day: # looking for the date according to the list
            days = days + 1
            
    if days == 1:  #return when the day matches
        return True
    else:
        return False 
        


def unique_month(month, possible_birthdays):
    
    months = 0
    for j in range(len(possible_birthdays)):  #creating the for loop for the range of possible birthday months 
        
        if possible_birthdays[j][0] == month:# looking for the month according to the list
            months = months + 1
    if months == 1: #return when the month matches
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    
    tup = () 
    
    for k in range(len(possible_birthdays)):
        if possible_birthdays[k][0] == month:
            tup = tup + (possible_birthdays[k],)
            
    for l in range(len(tup)):
        if unique_day(tup[l][1], possible_birthdays):
            return True
    return False 
