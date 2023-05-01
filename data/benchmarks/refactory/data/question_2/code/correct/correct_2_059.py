def unique_day(day, possible_birthdays):
    count = 0
    for x in possible_birthdays:
      if day == x[1]:
        count += 1
    if count == 1:
      return True
    else:
      return False
      
def unique_month(month, possible_birthdays):
    count = 0
    for x in possible_birthdays:
      if month == x[0]:
        count += 1
    if count == 1:
      return True
    else:
      return False

def contains_unique_day(month, possible_birthdays):
  possible_days = ()
  for x in possible_birthdays:
    if x[0] == month:
      possible_days += (x,)
  for day in possible_days:
    if unique_day(day[1], possible_birthdays) == True:
      return True
  else:
    return False
