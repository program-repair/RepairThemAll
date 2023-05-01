def unique_day(day, possible_birthdays):
	unique_num = 0
	for i in possible_birthdays:
		if i[1] == day:
			unique_num = unique_num + 1
		else:
			unique_num= unique_num + 0
	if unique_num > 1:
		return False
	else:
		return True

def unique_month(month, possible_birthdays):
	unique_num = 0
	for i in possible_birthdays:
		if i[0] == month:
			unique_num = unique_num + 1
		else:
			unique_num= unique_num + 0
	if unique_num > 1:
		return False
	else:
		return True

def contains_unique_day(month, possible_birthdays):
	days_in_month = ()
	days_not_in_month = ()
	unique_days = ()
	for row in possible_birthdays:
		if row[0] == month:
			days_in_month = days_in_month + (row[1],)
		else:
			days_not_in_month = days_not_in_month + (row[1],)
	
	for row2 in days_in_month:
		if row2 in days_not_in_month:
			continue
		else:
			unique_days = unique_days + (row2,)
	if unique_days == ():
		return False
	else:
		return True
