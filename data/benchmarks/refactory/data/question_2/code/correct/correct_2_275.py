def unique_day(date, possible_birthdays):
    days = [birthday[1] for birthday in possible_birthdays]
    return days.count(date) == 1

def unique_month(month, possible_birthdays):
    months = [birthday[0] for birthday in possible_birthdays]
    return months.count(month) == 1

def contains_unique_day(month, possible_birthdays):
    days = list(filter(lambda x: x[0] == month, possible_birthdays))
    for day in days:
        if unique_day(day[1], possible_birthdays):
            return True
    return False
