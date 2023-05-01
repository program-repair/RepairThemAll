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
    for i in range(len(possible_birthdays)):
        if month==possible_birthdays[i][0]:
            new_possible_birthdays+=(possible_birthdays[i],)
        new_day=""
        counter=0
        for n in range(len(possible_birthdays)):
            if unique_day(new_day,possible_birthdays)==True:
                counter+=1
            if counter==0:
                return False
            else:
                return True 
    
