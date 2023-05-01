def unique_day(day, possible_birthdays):
    a= tuple(filter(lambda birthday: day == birthday[1], possible_birthdays))

    return (len(a) ==1) 

def unique_month(month, possible_birthdays):
    a= tuple(filter(lambda birth_month: month == birth_month[0], possible_birthdays))

    return (len(a) ==1) 
    
def contains_unique_day(month, possible_birthdays):
    #filter out month
    a = filter(lambda birth_month: month == birth_month[0], possible_birthdays)
    for i in a:
        if unique_day(i[1],possible_birthdays):
            return True

    return False 
