def count_dates(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[1] == date:
            count += 1
    return count
    
def unique_day(date, possible_birthdays):
    if count_dates(date, possible_birthdays) == 1:
        return True
    else:
        return False
    
def count_months(month, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if i[0] == month:
            count += 1
    return count
    
def unique_month(month, possible_birthdays):
    if count_months(month, possible_birthdays) == 1:
        return True
    else:
        return False

def days(month, possible_birthdays):
    days_in_month = ()
    for i in possible_birthdays:
        if i[0] == month:
            days_in_month += (i[1],)
    return days_in_month

def contains_unique_day(month, possible_birthdays):
    for x in days_in_month:
        if unique_day(x, possible_birthdays):
            return True
        else:
            return False
                
        
    
    
    
   
