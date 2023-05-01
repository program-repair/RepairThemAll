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
    for birthday in possible_birthdays:
        if birthday[0] == month and unique_day(birthday[1], possible_birthdays) == True:
            return True
    return False
