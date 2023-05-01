def unique_day(date, possible_birthdays):
    flag = 0
    for i in possible_birthdays:
        if i[1] == date:
            flag += 1

    return True if flag == 1 else False

def unique_month(month, possible_birthdays):
    flag = 0
    for i in possible_birthdays:
        if i[0] == month:
            flag += 1

    return True if flag == 1 else False

def contains_unique_day(month, possible_birthdays):
    flag = 0
    unique_days = []

    for i in possible_birthdays:
        if i[1] not in unique_days:
            unique_days.append(i[1])
        else:
            unique_days.remove(i[1])

    for i in possible_birthdays:
        if i[0] == month and i[1] in unique_days:
            return True

    return False 
