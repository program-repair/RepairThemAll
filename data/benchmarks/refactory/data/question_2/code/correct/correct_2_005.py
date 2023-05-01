def unique_day(day, possible_birthdays):
    def dayfilter(birthday):
        if birthday[1] == day:
            return True
        else:
            return False
    possible = tuple(filter(dayfilter,possible_birthdays))
    if len(possible) == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    def monthfilter(birthday):
        if birthday[0] == month:
            return True
        else:
            return False
    possible = tuple(filter(monthfilter,possible_birthdays))
    if len(possible) == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    def monthfilter(birthday):
        if birthday[0]==month:
            return True
        else:
            return False
    possible = tuple(filter(monthfilter,possible_birthdays))
    def daymap(birthday):
        return birthday[1]
    possibledays = tuple(map(daymap,possible))
    result = False
    for n in range(0,len(possibledays)):
        if unique_day(possibledays[n],possible_birthdays):
            result = True
    return result
