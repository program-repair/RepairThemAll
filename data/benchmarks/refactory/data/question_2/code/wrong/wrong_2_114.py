def unique_day(day, possible_birthdays):
	check = 0
	for birthday in possible_birthdays:
		if birthday[1] == day:
			check = check + 1
	if check > 1 :
		return False
	else:
		return True


def unique_month(month, possible_birthdays):
	check = 0
	for birthday in possible_birthdays:
		if birthday[0] == month:
			check = check + 1
	if check > 1 :
		return False
	else:
		return True
		
def contains_unique_day(month, possible_birthdays):
	for birthday in possible_birthdays:
		if month == birthday[0] and unique_day(birthday[1], possible_birthdays):
				return True
	else:
		return False
