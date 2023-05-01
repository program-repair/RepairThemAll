def unique_day(day, possible_birthdays):
    for i in range (len(possible_birthdays)):
        if possible_birthdays[i][1] == day:
            for j in range (i + 1, len(possible_birthdays)):
                if possible_birthdays[j][1] == day:
                    return False
    return True
def unique_month(month, possible_birthdays):
    for i in range (len(possible_birthdays)):
        if possible_birthdays[i][0] == month:
            for j in range (i + 1, len(possible_birthdays)):
                if possible_birthdays[j][0] == month:
                    return False
    return True
def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0] == month:
            if unique_day(i[1], possible_birthdays):
                return True
    return False 
