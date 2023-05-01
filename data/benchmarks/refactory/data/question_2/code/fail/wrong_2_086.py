def unique_day(day, possible_birthdays):
    counted = ()
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            if day not in counted:
                counted += (day,)
            else:
                return False
    
    return True
