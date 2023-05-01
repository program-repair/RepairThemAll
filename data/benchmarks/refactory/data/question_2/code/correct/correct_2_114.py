def unique_day(day, possible_birthdays):
    days = tuple(map(lambda x: x[1], possible_birthdays))
    count = 0
    for temp_day in days:
        if temp_day == day:
            count+=1
    return True if count == 1 else False

def unique_month(month, possible_birthdays):
    months = tuple(map(lambda x: x[0], possible_birthdays))
    count = 0
    for temp_month in months:
        if temp_month==month:
            count+=1
    return True if count == 1 else False

def contains_unique_day(month, possible_birthdays):
    temp_days = tuple(map(lambda x: x[1] ,filter(lambda x: x[0]==month,possible_birthdays)))
    for temp_day in temp_days:
        if unique_day(temp_day, possible_birthdays):
            return True
    return False
