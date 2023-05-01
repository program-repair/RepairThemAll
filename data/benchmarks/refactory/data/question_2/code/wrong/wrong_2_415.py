def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if day==i[1]:
            count+=1
    if count>1:
        return False
    else:
        return True

def unique_month(month, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if month==i[0]:
            count+=1
    if count>1:
        return False
    else:
        return True
        
def contains_unique_day(month, possible_birthdays):
    bday=()
    for i in possible_birthdays:
        if month==i[0]:
            bday+=(i,)
    for i in bday:
        if unique_day(i[1],possible_birthdays):
            return True
    else:
        return False

