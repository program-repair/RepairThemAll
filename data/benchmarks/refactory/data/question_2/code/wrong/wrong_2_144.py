def unique_day(date, possible_birthdays):
    count = 0
    for i in possible_birthdays:
        if day == i[1]:
            count += 1
    return count == 1

def unique_month(month, possible_birthdays):
    count = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            count += 1
    return count == 1
    
def contains_unique_day(month, possible_birthdays):
    singlemonthbirthday = ()
    for birthmonth in possible_birthdays:
        if month == birthmonth[0]:
            singlemonthbirthday += (birthmonth,)
    for birthday in singlemonthbirthday:
        if unique_day(birthday[1], possible_birthdays) == True:
            return True
    return False
