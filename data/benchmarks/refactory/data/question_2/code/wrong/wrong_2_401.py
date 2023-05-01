def unique_day(date, possible_birthdays):
    i=0
    count=0
    while i <= len(possible_birthdays):
        if possible_birthdays[i][1]==date:
            count+=1
            i+=1
    if count==1:
        return True
    else:
        return False
    
def unique_month(month, possible_birthdays):
    count=0
    for i in range(len(possible_birthdays)):
        if possible_birthdays[i][0]==month:
            count+=1
    if count==1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    if month=='June':
        return True
    elif month=='May':
        return True
    else:
        return False
