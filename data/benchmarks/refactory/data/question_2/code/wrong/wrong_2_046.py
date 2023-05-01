def unique_day(day, possible_birthdays):
	num=0
	for i in possible_birthdays:
		if day==i[1]:
			num=num+1
	if num==1:
		return True

	else:
		return False
		
def unique_month(month, possible_birthdays):
	num=0
	for i in possible_birthdays:
		if month==i[0]:
			num=num+1
	if num==1:
		return True

	else:
		return False

def contains_unique_day(month, possible_birthdays):
	result=()
	for i in possible_birthdays:
		if unique_day(i[1],possible_birthdays)==True:
			result=result+(i[0],)
	num=0
	for j in result:
		if month==j:
			num=num+1
	if num==1:
		return True
	else:
		return False

