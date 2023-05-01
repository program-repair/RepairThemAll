def unique_day(date, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        list = [x for x in possible_birthdays[i][1]]
        list = sorted(list)
        if date == list[i] and date != list[i+1] and date != list[i-1]:
            return True
        else:
            return False
                
def unique_month(month, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        list = [x for x in possible_birthdays[i][0]]
        list = sorted(list)
        if month == list[i] and month != list[i+1] and month != list[i-1]:
            return True
        else:
            return False

def contains_unique_day(month, possible_birthdays):
    return 
