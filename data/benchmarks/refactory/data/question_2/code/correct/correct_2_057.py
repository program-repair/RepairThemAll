def map(fn, seq):
    res = ()
    for ele in seq:
        res = res + (fn(ele), )
    return res

def filter(pred, seq):
    res = ()
    for ele in seq:
        if pred(ele):
            res = res + (ele, )
    return res
    
def unique_day(day, possible_birthdays):
    possible_days=map(lambda x:x[1],possible_birthdays)
    def count(day,possible_days):
        count_day=0
        for i in possible_days:
            if i==day:
                count_day=count_day+1
        return count_day
    return count(day,possible_days)==1

def unique_month(month, possible_birthdays):
    possible_months=map(lambda x:x[0],possible_birthdays)
    def count(month,possible_months):
        count_month=0
        for i in possible_months:
            if i==month:
                count_month=count_month+1
        return count_month
    return count(month,possible_months)==1

def contains_unique_day(month, possible_birthdays):
    tuple_with_unique_day=filter(lambda x:unique_day(x[1],possible_birthdays)==True,possible_birthdays)
    month_with_unique_day=map(lambda x:x[0],tuple_with_unique_day)
    return month in month_with_unique_day
