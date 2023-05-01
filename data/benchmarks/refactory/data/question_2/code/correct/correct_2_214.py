def unique_day(day, possible_birthdays):
	return len(tuple(filter(lambda y: day == y, 
	map(lambda x: x[1], possible_birthdays)))) == 1

def unique_month(month, possible_birthdays):
	return len(tuple(filter(lambda y: month == y, 
	map(lambda x: x[0], possible_birthdays)))) == 1

def contains_unique_day(month, possible_birthdays):
	return len(tuple(filter(lambda x: unique_day(x[1], possible_birthdays), 
		filter(lambda y: y[0] == month, possible_birthdays)))) > 0
