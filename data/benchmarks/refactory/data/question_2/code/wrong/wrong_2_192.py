def unique_day(day, possible_birthdays):
    i=0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            i+=1
            if i == 2:
                return False
    return True

def unique_month(month, possible_birthdays):
    i=0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            i+=1
            if i == 2:
                return False
    return True

def contains_unique_day(month, possible_birthdays):
    bday_list=()
    for birthday in possible_birthdays:
        if month == birthday[0]:
            bday_list+=(birthday,)
    for birthday in bday_list:
        if unique_day(birthday[1], possible_birthdays):
            return True
    return False
