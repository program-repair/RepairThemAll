def statement1(birthday, possible_birthdays):
    A = unique_month(birthday[0],possible_birthdays)
    B = contains_unique_day(birthday[0], possible_birthdays)
    
    if A == False and B == False:
        return True
    
    return False

def statement2(birthday, possible_birthdays):
    C = unique_day(birthday[1],possible_birthdays)
    
    if C == True:
        return True
    
    return False    

def statement3(birthday, possible_birthdays):
    D = unique_month(birthday[0],possible_birthdays)
    
    if D == True:
        return True
    
    return False
