def unique_day(day, possible_birthdays):
    count=0
    for i in possible_birthdays:
        count+=i.count(day)
    if count==1:
        return True
    return False

def unique_month(month, possible_birthdays):
    count=0
    for i in possible_birthdays:
        count+=i.count(month)
    if count==1:
        return True
    return False

def contains_unique_day(month, possible_birthdays):
    tup=tuple(filter(lambda x: x[0]==month,possible_birthdays))
    for i in range(len(tup)):
        if unique_day(tup[i][1],possible_birthdays)==True:
            return True
    return False
