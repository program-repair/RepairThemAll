def unique_day(date, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[1] == date:
            result = result + 1
    if result != 1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    result = 0
    for n in possible_birthdays:
        if n[0] == month:
            result = result + 1
    if result != 1:
        return False
    else:
        return True
    

def contains_unique_day(month, possible_birthdays):
    new_possible_birthdays = ()
    for n in range(len(possible_birthdays)):
        if month == possible_birthdays[n][0]:
            new_possible_birthdays += (possible_birthdays[i], )
    new_day = ""
    counter = 0
    for i in range(len(new_possible_birthdays)):
        new_day = new_possible_birthdays[i][1]
        if  unique_day(new_day, possible_birthdays) == True:
            counter = counter + 1
        if counter == 0:
            return False
        else:
            return True
            

