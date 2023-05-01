def unique_day(day, possible_birthdays):
    checker=0
    for k in possible_birthdays:
        if k[1]==day:
          checker+=1
    return checker==1
    
def unique_month(day, possible_birthdays):
    checker=0
    for k in possible_birthdays:
        if k[0]==day:
          checker+=1
    return checker==1
    
def contains_unique_day(month, possible_birthdays):
    return 
