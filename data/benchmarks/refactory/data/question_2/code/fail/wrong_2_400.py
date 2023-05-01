def unique_day(day, possible_birthdays):
    store = 0
    for i in possible_birthdays:
        if i[1] == day:
            if store == 1:
                return False
            else:
                store += 1
    return True

def unique_month(month, possible_birthdays):
    store = 0
    for i in possible_birthdays:
        if i[0] == month:
            if store == 1:
                return False
            else:
                store += 1
    return True

def contains_unique_day(month, possible_birthdays):
    def generate_unique_days(possible_birthdays):
        generate = ()
        for i in range(14, 20):
            if unique_day(str(i), possible_birthdays):
                generate += (str(i),)
        return generate
    for i in possible_birthdays:
        if i[0] == month:
            if str(i[1]) in generate_unique_days(possible_birthdays):
                return True
    return False
