def unique_day(day, possible_birthdays):
    #generate boolean array of whether tuple matches day
    days = sum(map(lambda x: x[1]==day,possible_birthdays))
    return days == 1

def unique_month(month, possible_birthdays):
    #generate boolean array of whether tuple matches month
    months = sum(map(lambda x: x[0]==month,possible_birthdays))
    return months == 1

def contains_unique_day(month, possible_birthdays):
    this_month = filter(lambda x: x[0]==month,possible_birthdays)
    days_in_this_month = tuple(map(lambda x: x[1],this_month))
    for i in range(1,31):
        if unique_day(str(i),possible_birthdays) and str(i) in days_in_this_month:
            return True
    return False

