def unique_day(day, possible_birthdays):
    result=()
    counter=0
    for i in possible_birthdays:
        if day==i[1]:
            result=result+(possible_birthdays[:counter]+possible_birthdays[counter+1:])
            break
        else:
            counter+=1
            continue
    for i in result:
        if day==i[1]:
            return False
    return True

def unique_month(month, possible_birthdays):
    result=()
    counter=0
    for i in possible_birthdays:
        if month==i[0]:
            result=result+(possible_birthdays[:counter]+possible_birthdays[counter+1:])
            break
        else:
            counter+=1
            continue
    for i in result:
        if month==i[0]:
            return False
    return True

def contains_unique_day(month, possible_birthdays):
    result=()
    for i in possible_birthdays:
        if i[0]==month:
            result+=(i,) #result should contain all the birthdays with the specified month.
    for i in result:
        if unique_day(i[1],possible_birthdays)==True:
            return True
    return False
