def statement1(birthday, possible_birthdays):
    x = unique_month(birthday[0],possible_birthdays)
    y = contains_unique_day(birthday[0], possible_birthdays)
    
    if x == False and y == False:
        return True
    
    return False

def statement2(birthday, possible_birthdays):
    z = unique_day(birthday[1],possible_birthdays)
    
    if z == True:
        return True
    

    return False    

def statement3(birthday, possible_birthdays):
    q = unique_month(birthday[0],possible_birthdays)
    
    if q == True:
        return True
    
    return False  
