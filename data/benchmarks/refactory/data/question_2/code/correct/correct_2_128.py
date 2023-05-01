def unique_day(day, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if day == birthday[1]:
            counter += 1            
    return counter == 1

def unique_month(month, possible_birthdays):
    counter = 0
    for birthday in possible_birthdays:
        if month == birthday[0]:
            counter += 1
    return counter == 1

def contains_unique_day(month, possible_birthdays):
    truth_holder = False
    for birthday in possible_birthdays:
        if birthday[0] != month:
            continue
        else:
            truth_holder = truth_holder or unique_day(birthday[1], possible_birthdays)
    return truth_holder
