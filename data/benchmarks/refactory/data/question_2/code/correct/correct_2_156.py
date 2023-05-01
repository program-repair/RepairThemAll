def unique_day(day, possible_birthdays):
    counter =0
    for elements in possible_birthdays:
        if day == elements[1]:
            counter +=1
    return counter == 1

def unique_month(month, possible_birthdays):
    counter =0
    for elements in possible_birthdays:
        if month == elements[0]:
            counter +=1
    return counter == 1

def contains_unique_day(month, possible_birthdays):
    tupleofdays=()
    for elements in possible_birthdays:
        if elements[0]==month:
            tupleofdays += (elements[1],)
    for elements in tupleofdays:
        if unique_day(elements,possible_birthdays):
            return True
    return False
