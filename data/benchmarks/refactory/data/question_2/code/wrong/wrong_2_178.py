def unique_day(day, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[1] == day:
            if counter >= 1:
                return False
            else:
                counter += 1
    return True

def unique_month(month, possible_birthdays):
    counter = 0
    for i in possible_birthdays:
        if i[0] == month:
            if counter >= 1:
                return False
            else:
                counter += 1
    return True

def contains_unique_day(month, possible_birthdays):
    filtered = tuple(filter(lambda x: x[0] == month, possible_birthdays))
    tup1 = tuple(filter(lambda x: x[0] != month, possible_birthdays)) # Remaining dates
    tup2 = tuple(map(lambda x: x[1], tup1)) # Day of the remaining dates
    def unique(tup):
        output = ()
        for i in tup:
            if i not in output:
                output += (i,)
        return output
    dates = unique(tup2)
    
    for i in filtered:
        if i[1] not in dates:
            return True
    return False
