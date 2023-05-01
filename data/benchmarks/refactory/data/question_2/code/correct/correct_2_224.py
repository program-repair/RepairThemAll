def unique_day(day, possible_birthdays):
    bag = []
    for birthdays in possible_birthdays:
        if birthdays[1] == day:
            bag.append(day)
    n = len(bag)
    if n == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    bag = []
    for months in possible_birthdays:
        if months[0] == month:
            bag.append(month)
    n = len(bag)
    if n == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    bag = ()
    for months in possible_birthdays:
        if months[0] == month:
            bag += ((months[1]),)
    for days in bag:
        if unique_day(days,possible_birthdays):
            return True
    else:
        return False
