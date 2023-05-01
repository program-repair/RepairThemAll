def unique_day(day, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if day==i[1]:
            num+=1
    return num==1

def unique_month(month, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if month==i[0]:
            num+=1
    return num==1

def contains_unique_day(month, possible_birthdays):
    days=()
    for i in possible_birthdays:
        if month==i[0]:
            if unique_day(i[1],possible_birthdays):
                days = days + (i[1],)
    return len(days)==1
