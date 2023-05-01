def unique_day(date, possible_birthdays):
    count=0
    for i in possible_birthdays: 
        if i[0]==possile_birthdays[1]:
            count+=1
    if count==possible_birthdays[1]:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    if month in possible_birthdays[0]:
        return False
    else:
        return True

def contains_unique_day(month, possible_birthdays):
    if not unique_day and not unique_month: 
        return False
    else: 
        return True 
