def unique_day(day, possible_birthdays):
    birthday_with_day = list(filter(lambda birthday: birthday[1] == day \
                                 , possible_birthdays))
    if len(birthday_with_day) >= 2:
        return False
    return True

def unique_month(month, possible_birthdays):
    birthday_with_month = list(filter(lambda birthday: birthday[0] == month \
                                 , possible_birthdays))
    if len(birthday_with_month) >= 2:
        return False
    return True

def contains_unique_day(month, possible_birthdays):
    birthday_with_month = list(filter(lambda birthday: birthday[0] == month \
                                 , possible_birthdays))
    birthday_day = list(map(lambda birthday: birthday[1], birthday_with_month))
    unique_day_list = list(filter(lambda day: unique_day(day, possible_birthdays)\
                                  , birthday_day))
    return len(unique_day_list) > 0
