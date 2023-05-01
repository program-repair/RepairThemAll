def unique_day(day, possible_birthdays):
    checker=True
    for k in possible_birthdays:
        if k[1]==day:
          checker=False
    return checker

def unique_month(day, possible_birthdays):
    checker=True
    for k in possible_birthdays:
        if k[0]==day:
          checker=False
    return checker
    
def contains_unique_day(month, possible_birthdays):
    return 
