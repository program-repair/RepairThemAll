def remove_extras(lst):
	new_lst = []
	for element in lst:
		if (element in lst) and (element not in new_lst):
					 new_lst.append(element)
		else:
		    continue
	return new_lst
