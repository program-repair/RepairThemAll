def unique_day(day, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if day==i[1]:
            counter=counter+1
        else:
            pass
    return counter<=1

def unique_month(month, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if month==i[0]:
            counter=counter+1
        else:
            pass
    return counter<=1

def contains_unique_day(month,possible_birthdays):
    tup=()
    for i in possible_birthdays:
        if unique_day(i[1],possible_birthdays):
            tup=tup+(i[0],)
        else:
            pass
    for k in range(0,len(tup)):
        if tup[k]==month:
            return True
        else:
            pass
    return False
