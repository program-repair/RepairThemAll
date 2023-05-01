def unique_day(date, possible_birthdays):
    counter=0
    for i in possible_birthdays:
        if i[1]==date:
            counter+=1
        else:
            counter=counter
    if counter==1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    counter=0
    for date in possible_birthdays:
        if date[0]==month:
            counter+=1
        else:
            counter=counter
    if counter==1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    date=()
    for mon in possible_birthdays:
        if month ==mon[0]:
            date+=(mon,)
        else:
            date=date
    days=()
    for day in date:
        days+=(day[1],)
    y=()
    for x in days:
        if unique_day(x, possible_birthdays)==True:
            y+=(x,)
        else:
            y=y
    if y==():
        return False
    else:
        return True 
