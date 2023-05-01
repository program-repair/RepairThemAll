def unique_day(day, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if i[1]==day: num+=1
    return num==1


def unique_month(month, possible_birthdays):
    num=0
    for i in possible_birthdays:
        if i[1]==month: num+=1
    return num==1

def contains_unique_day(month, possible_birthdays):
    for i in possible_birthdays:
        if i[0]==month and unique_day(i[1],possible_birthdays):
            return True
    return False
