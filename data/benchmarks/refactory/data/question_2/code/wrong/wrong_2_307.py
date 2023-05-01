def unique_day(date, possible_birthdays):
    count=0
    for date in birthday[(len(possible_birthdays))-1][1]:
        count += 1
        possible_birthday=possible_birthday[:(len(possible_birthdays))-1]
    if count==1:
        return True
    else:
        return False
    

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
