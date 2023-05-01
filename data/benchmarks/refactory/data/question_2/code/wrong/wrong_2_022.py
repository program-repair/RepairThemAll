def unique_day(day, possible_birthdays):
    index = 1
    for days in tuple(map(lambda x:x[1], possible_birthdays)):
        if day == days:
            index = index*(-1)
            if index == 1:
                return False
    return True

def unique_month(month, possible_birthdays):
    index = 1
    for months in tuple(map(lambda x:x[0], possible_birthdays)):
        if month == months:
            index = index*(-1)
            if index == 1:
                return False
    return True
    
def contains_unique_day(month, possible_birthdays):
    birthday_list = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    for i in tuple(map(lambda x: x[1], birthday_list)):
        if unique_day(i,possible_birthdays):
            return True
    return False
