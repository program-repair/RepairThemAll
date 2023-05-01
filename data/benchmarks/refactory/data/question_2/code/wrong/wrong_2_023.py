def unique_day(day, possible_birthdays):
    count = 0
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            count +=1
            if count == 2:
                return False
    return True

def unique_month(month, possible_birthdays):
    count = 0
    for birthdays in possible_birthdays:
        if birthdays[0] == month:
            count +=1
            if count == 2:
                return False
    return True

def contains_unique_day(month, possible_birthdays):
    count = ()
    for birthdays in possible_birthdays:
        if birthdays[0] == month:
            count += (birthdays,)
    for sub_birthday in count:
        if unique_day(sub_birthday[1], possible_birthdays):
            return True
    return False 
