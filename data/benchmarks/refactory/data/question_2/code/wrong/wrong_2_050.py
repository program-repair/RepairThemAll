def unique_day(date, possible_birthdays):
    for x in range(len(1,possible_birthdays + 1)):
        for i in possible_birthdays[x][1]:
            if i == possible_birthdays[0][1]:
                return False
            else:
                return i == unique_day(date,possible_birthdays[2:][1])

def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
