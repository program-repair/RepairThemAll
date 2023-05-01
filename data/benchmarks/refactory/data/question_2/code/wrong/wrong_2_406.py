def unique_day(day, possible_birthdays):
    
    tupleofdays = ()
    for i in possible_birthdays:
        tupleofdays += (i[1],)

    count = 0
    for i in tupleofdays:
        if day == i:
            count += 1

    return count == 1

def unique_month(month, possible_birthdays):
    tupleofmonths = ()
    for i in possible_birthdays:
        tupleofmonths += (i[0],)

    count = 0

    for i in tupleofmonths:
        if month == i:
            count += 1

    return count ==1

def contains_unique_day(month, possible_birthdays):
##    """Your solution here"""

    for i in possible_birthdays:
        if unique_day(i[1], possible_birthdays) == True:
            ans = False
            if i[0] == month:
                ans = True
                break
            else:
                continue
        else:
            continue

    return ans
