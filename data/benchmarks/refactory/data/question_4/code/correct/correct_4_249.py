def sort_age(lst):
	age_list = []
	result = ()
	for x in lst:
		age_list.append(list(x))
	sort = []
	while age_list:
		largest = age_list[0]
		for element in age_list:
			if element[1] > largest[1]:
				largest = element
		age_list.remove(largest)
		sort.append(largest)
	for x in sort:
		result += ((x[0],x[1]),)
	return list(result)
