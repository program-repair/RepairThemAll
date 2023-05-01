def unique_day(day, possible_birthdays):
    days = tuple(map(lambda x: x[1],possible_birthdays))
    count = 0
    for i in days:
        if i == day:
            count = count+1
    return count == 1

def unique_month(month, possible_birthdays):
    months = tuple(map(lambda x: x[0],possible_birthdays))
    count = 0
    for i in months:
        if i == month:
            count = count +1
    return count ==1
    
def contains_unique_day(month, possible_birthdays):
    specific_set = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    get_days = tuple(map(lambda x: x[1],specific_set))
    ans = tuple(map(lambda x: unique_day(x,possible_birthdays),get_days))
    if True in ans:
        return True
    else:
        return False
