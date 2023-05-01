def unique_day(day, possible_birthdays):
    n=0
    for i in range (len(possible_birthdays)):
        if day == possible_birthdays[i][1]:
            n+=1
        else:
            n=n
    return n == 1

def unique_month(month, possible_birthdays):
    n=0
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays[i][0]:
            n+=1
        else:
            n=n
    return n == 1

def contains_unique_day(month, possible_birthdays):
    new_tup = ()
    edited_tup = ()
    for i in range (len(possible_birthdays)):
        if month == possible_birthdays [i][0]:
            new_tup = new_tup + ((possible_birthdays[i][0],possible_birthdays[i][1]),)

    for i in range (len(possible_birthdays)):
        if month != possible_birthdays [i][0]:
            edited_tup = edited_tup + ((possible_birthdays[i][0],possible_birthdays[i][1]),)
    #print(new_tup)
    #print(edited_tup)

    def checker (new_tup, edited_tup):
        result = False
        for j in range (len(new_tup)):
            inter_result = False
            for k in range (len(edited_tup)):
                bool_tup = (new_tup[j][1] == edited_tup[k][1])
                inter_result = inter_result or bool_tup
            result = result or inter_result
            result = not result
        return result
    return checker (new_tup, edited_tup)
