def unique_day(date, possible_birthdays):
    bdaylist = possible_birthdays
    count = 0
    while len(bdaylist) > 0:
        single = bdaylist[0]
        if single[1] == day:
            count = count + 1
        if count == 2:
            return False
            break
        bdaylist = bdaylist[1:]
    return True

def unique_month(month, possible_birthdays):
    bdaylist = possible_birthdays
    count = 0
    while len(bdaylist) > 0:
        single = bdaylist[0]
        if single[0] == month:
            count = count + 1
        if count == 2:
            return False
            break
        bdaylist = bdaylist[1:]
    return True

def contains_unique_day(month, possible_birthdays):
    month_list = ()
    bday_list = possible_birthdays
    while len(bday_list)>0:
        if bday_list[0][0]==month:
            month_list = month_list + (bday_list[0],)
        bday_list = bday_list[1:]
    
    while len(month_list)>0:
        if unique_day(month_list[0][1],possible_birthdays):
            return True
        month_list = month_list[1:]
    return False

