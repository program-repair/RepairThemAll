def unique_day(day, possible_birthdays):
    counter=0
    for birthday in possible_birthdays:
        if day==birthday[1]:
            counter+=1
        else:
            continue
    if counter==1:
        return True
    else:
        return False
def unique_month(month, possible_birthdays):
    counter=0
    for birthday in possible_birthdays:
        if month==birthday[0]:
            counter+=1
        else:
            continue
    if counter==1:
        return True
    else:
        return False
def filter_1(pred,seq):
    if seq==():
        return ()
    elif pred(seq[0]):
        return (seq[0],) + filter_1(pred,seq[1:])
    else:
        return filter_1(pred,seq[1:])
    
def contains_unique_day(month, possible_birthdays):
    month_dates=filter_1(lambda x:True if x[0]==month else False, possible_birthdays)
    for date in month_dates:
        if unique_day(date[1],possible_birthdays):
            return True
        else:
            continue
    else:
        return False
