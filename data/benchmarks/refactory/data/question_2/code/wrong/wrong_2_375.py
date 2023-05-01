def unique_day(date, possible_birthdays):
    count=0
    for i in possible_birthdays: 
        if i[1]==date:
            count+=1
    if count!=1:           #if not can put count==1
        return False
    else:
        return True
   

def unique_month(month, possible_birthdays):
    count=0
    for i in possible_birthdays:
        if i[0]==month:
            count+=1
    if count!= 1:
        return False 
    else:
        return True
   

def contains_unique_day(month, possible_birthdays):
    new_possible_birthdays=()
    for i in possible_birthdays[1]:
        if unique_day(date,possible_birthdays)==true:
            new_possible_birthdays+=(possible_birthdays[i],)
        new_month=()
        counter=0
        for n in possible_birthdays[0]:
            if month==possible_birthday[i][0]:
                counter+=1
            if counter==0:
                return False
            else: 
                return True 
