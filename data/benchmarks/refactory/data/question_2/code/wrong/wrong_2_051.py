def unique_day(date, possible_birthdays):
    for x in range(1,len(possible_birthdays)):
        for i in possible_birthdays[x][1]:
            if possible_birthdays[0][1] == possible_birthdays[i][1]:
                return False
            else:
                return unique_day(date,possible_birthdays[1:])
def unique_month(month, possible_birthdays):
    return

def contains_unique_day(month, possible_birthdays):
    return 
