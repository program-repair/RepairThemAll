def unique_day(day, possible_birthdays):
    def get_day(birthday):
        return birthday[1]
    count = 0
    for i in possible_birthdays:
        if get_day(i) == day:
            count +=1
        else:
            continue
    if count == 1:
        return True
    else:
        return False


def unique_month(month, possible_birthdays):
    def get_month(birthday):
        return birthday[0]
    count = 0
    for i in possible_birthdays:
        if get_month(i) == month:
            count +=1
        else:
            continue
    if count == 1:
        return True
    else:
        return False

def get_month(birthday):
        return birthday[0]
def get_day(birthday):
        return birthday[1]

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if get_month(i) == month and unique_day(get_day(i), possible_birthdays):
            return True
        else:
            continue
    return False 
