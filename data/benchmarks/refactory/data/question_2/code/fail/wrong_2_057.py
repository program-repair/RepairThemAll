def filter(pred, seq):
    if seq == ():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter(pred, seq[1:])
    else:
        return filter(pred, seq[1:])

def unique_day(date, possible_birthdays):
    counter = 0
    for bday in possible_birthdays:
        if date == bday[1]:
            counter += 1
    if counter > 1:
        return False
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for bday in possible_birthdays:
        if month == bday[0]:
            counter += 1
    if counter > 1:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    bdays_in_month = filter(lambda bday: bday[0] == month, possible_birthdays)
    for bday in bdays_in_month:
        if unique_day(bday[1], possible_birthdays):
            return True
    return False
