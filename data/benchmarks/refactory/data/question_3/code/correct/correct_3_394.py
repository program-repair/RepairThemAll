def remove_extras(lst):
	new_list = []
	for x in lst:
		if x not in new_list:
			new_list.append(x)
	return new_list
