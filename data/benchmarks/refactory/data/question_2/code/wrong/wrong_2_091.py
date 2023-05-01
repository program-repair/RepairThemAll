def unique_day(day, possible_birthdays):
    days = ()
    for all_days in possible_birthdays:
        days = days + (all_days[1],)
        i = 0
        for all_days in days:
            if all_days == day:
                i = i+1
    if i == 1:
        return True
    else:
        return False

def unique_month(month, possible_birthdays):
    months = ()
    for all_months in possible_birthdays:
        months = months + (all_months[0],)
        i = 0
        for all_months in months:
            if all_months == month:
                i = i+1
    if i == 1:
        return True
    else:
        return False

def contains_unique_day(month, possible_birthdays):
    May_days = ()
    June_days = ()
    July_days = ()
    August_days = ()
    May_dates = possible_birthdays[:3]
    for all_days in May_dates:
        May_days = May_days + (all_days[1],)
    June_dates = possible_birthdays[3:5]
    for all_days in June_dates:
        June_days = June_days + (all_days[1],)
    July_dates = possible_birthdays[5:7]
    for all_days in July_dates:
        July_days = July_days + (all_days[1],)
    August_dates = possible_birthdays[7:]
    for all_days in August_dates:
        August_days = August_days + (all_days[1],)
    if month == 'May': 
        for days in May_days:
            found_repeated = 0
            for check_day in June_days:
                if days == check_day:
                    found_repeated = 1
                    break
            if found_repeated == 0:
                for check_day in July_days:
                    if days == check_day:
                        found_repeated = 1
                        break
                if found_repeated == 0:
                    for check_day in August_days:
                        if days == check_day:
                            found_repeated = 1
                            break
    elif month == 'June':
        for days in June_days:
            found_repeated = 0
            for check_day in May_days:
                if days == check_day:
                    found_repeated = 1
                    break
            if found_repeated == 0:
                for check_day in July_days:
                    if days == check_day:
                        found_repeated = 1
                        break
                if found_repeated == 0:
                    for check_day in August_days:
                        if days == check_day:
                            found_repeated = 1
                            break
    elif month == 'July':
        for days in July_days:
            found_repeated = 0
            for check_day in May_days:
                if days == check_day:
                    found_repeated = 1
                    break
            if found_repeated == 0:
                for check_day in June_days:
                    if days == check_day:
                        found_repeated = 1
                        break
                if found_repeated == 0:
                    for check_day in August_days:
                        if days == check_day:
                            found_repeated = 1
                            break
    else:
        for days in August_days:
            found_repeated = 0
            for check_day in May_days:
                if days == check_day:
                    found_repeated = 1
                    break
            if found_repeated == 0:
                for check_day in June_days:
                    if days == check_day:
                        found_repeated = 1
                        break
                if found_repeated == 0:
                    for check_day in July_days:
                        if days == check_day:
                            found_repeated = 1
                            break
    if found_repeated == 0:
        return True
    return False
