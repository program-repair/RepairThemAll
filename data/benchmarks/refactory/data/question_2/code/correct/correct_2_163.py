def unique_day(day, possible_birthdays):
    c=0
    for birthday in possible_birthdays:
        if day==birthday[1]:
            c+=1
    return c==1

def unique_month(month, possible_birthdays):
    c=0
    for birthday in possible_birthdays:
        if month==birthday[0]:
            c+=1
    return c==1

def contains_unique_day(month, possible_birthdays):
    d=map(lambda birthday:birthday[1],filter(lambda birthday:birthday[0]==month,possible_birthdays))
    for day in d:
        if unique_day(day,possible_birthdays):
            return True
    return False
