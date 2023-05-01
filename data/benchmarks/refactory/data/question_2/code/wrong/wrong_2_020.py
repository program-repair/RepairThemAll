def unique_day(date, possible_birthdays):

    count =0

    for i in possible_birthdays:

        if date==i[1]:

            count+=1

    return count==1

def unique_month(month, possible_birthdays):

    count =0

    for i in possible_birthdays:

        if month==i[0]:

            count+=1

    return count==1

def contains_unique_day(month, possible_birthdays):

    daysinmonth=()

    count=0

    for i in possible_birthdays:

        if month==i[0]:

            daysinmonth+=(i[1],)

    for i in daysinmonth:

        if unique_day(i,possible_birthdays):
            count+=1

    return count==1
