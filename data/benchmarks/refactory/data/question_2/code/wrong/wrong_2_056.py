def unique_day(date, possible_birthdays):
    for i in range(0,len(possible_birthdays)):
        list_final = [x for x in possible_birthdays[i][1]]
        list_final = sorted(list_final)
        if date == list_final[i] and date != list_final[i+1] and date != list_final[i-1]:
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
    month_tuple = ()
    for i in range(0,len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            month_tuple = month_tuple + (possible_birthdays[i][1],)
    for x in month_tuple:
        for i in range(0,len(possible_birthdays)):
            if x == possible_birthdays[i][1]:
                return False
            else:
                return True
        
