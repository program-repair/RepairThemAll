def unique_day(day, possible_birthdays):
    data=()
    for birthday in possible_birthdays:
        if day == birthday[1]:
            data += (birthday,)
    if len(data)==1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    data = ()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            data += (birthday,)
    if len(data)==1:
        return True
    else:
        return False
        
def contains_unique_day(month, possible_birthdays):
    data, outcome = (),()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            data += (birthday,)
    for birthday in data:
        if unique_day(birthday[1], possible_birthdays) == True:
            outcome += birthday
        else:
            continue
    if outcome == ():
        return False
    else:
        return unique_day(outcome[1],possible_birthdays)
