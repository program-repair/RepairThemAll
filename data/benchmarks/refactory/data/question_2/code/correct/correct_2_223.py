def unique_day(day, possible_birthdays):
    s=0
    for b in possible_birthdays:
        if b[1]==day:
            s=s+1
        else:
            continue
    return s==1

def unique_month(month, possible_birthdays):
    s=0
    for b in possible_birthdays:
        if b[0]==month:
            s=s+1
        else:
            continue
    return s==1

def contains_unique_day(month, possible_birthdays):
    a=0
    for b in possible_birthdays:
        if b[0]==month:
            s=b[1]
            if unique_day(s,possible_birthdays):
                a=a+1
                break
            else:
                continue
        else:
            continue
    if a==1:
        return True
    else:
        return False
