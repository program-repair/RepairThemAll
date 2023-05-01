def unique_day(day, possible_birthdays):

    count = 0

    for i in possible_birthdays:
        if day in i:
            count += 1
            
    if count == 1:
        return True
    else:
        return False
        
        
def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
